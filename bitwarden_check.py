#!/usr/bin/env python3

import json
import sys
import signal
import argparse
from datetime import datetime, timezone, timedelta

try:
    from colorama import Fore, Style, init
except ImportError:
    print("This script requires 'colorama'. Install it with:\n  pip install colorama")
    sys.exit(1)

# ✅ Handle BrokenPipeError properly
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

init(autoreset=True)

# ======================
# ✅ ARGUMENT PARSING
# ======================

parser = argparse.ArgumentParser(
    description="Show Bitwarden items older than a given number of days."
)
parser.add_argument("file", help="Bitwarden JSON export file")
parser.add_argument(
    "--older-than",
    type=int,
    default=182,
    help="Only show items older than this many days (default: 182)"
)
args = parser.parse_args()

# ======================
# ✅ LOAD DATA
# ======================

with open(args.file) as f:
    data = json.load(f)

folder_map = {f['id']: f['name'] for f in data['folders']}

output = {
    'Top Secret': [],
    'Secret': [],
    'No Folder': []
}

# ======================
# ✅ AGE THRESHOLDS
# ======================

now = datetime.now(timezone.utc)
one_year = now - timedelta(days=365)
six_months = now - timedelta(days=182)
custom_threshold = now - timedelta(days=args.older_than)

# ======================
# ✅ PROCESS ITEMS
# ======================

for item in data['items']:
    if not item.get('login'):
        continue

    folder_id = item.get('folderId')
    folder_name = folder_map.get(folder_id, 'No Folder')

    if folder_name == 'Archived':
        continue

    rev_date_str = item.get('revisionDate')
    rev_date = datetime.fromisoformat(rev_date_str.replace("Z", "+00:00")) if rev_date_str else now

    # ✅ Filter: only include if older than custom threshold
    if rev_date > custom_threshold:
        continue

    output.setdefault(folder_name, []).append({
        'name': item.get('name'),
        'revisionDate': rev_date_str,
        'url': item['login']['uris'][0]['uri'] if item['login']['uris'] else '',
    })

# ======================
# ✅ PRINT RESULTS
# ======================

folder_order = ['Top Secret', 'Secret', 'No Folder']

for folder in folder_order:
    items = output.get(folder, [])
    if not items:
        continue

    # Sort oldest first
    items.sort(key=lambda x: x['revisionDate'] or '')

    # Solid line header with 📂
    header = f"{Fore.CYAN}{Style.BRIGHT}📂  ━━ {folder.upper()} ━━{Style.RESET_ALL}"
    print("\n" + header + "\n")

    for entry in items:
        rev_date_str = entry['revisionDate']
        rev_date = datetime.fromisoformat(rev_date_str.replace("Z", "+00:00")) if rev_date_str else now

        # ✅ Color is independent: red if >1yr, yellow if >6mo, else green
        if rev_date < one_year:
            icon = "🔴"
            color = Fore.RED
        elif rev_date < six_months:
            icon = "🟡"
            color = Fore.YELLOW
        else:
            icon = "🟢"
            color = Fore.GREEN

        indent = "  "
        print(f"{indent}{color}{icon} Name: {entry['name']}")
        print(f"{indent}{color}Last Modified: {rev_date_str}")
        print(f"{indent}{color}URL: {entry['url']}\n")
