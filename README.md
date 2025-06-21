# Bitwarden Check

## Description

Shows entries in a Bitwarden export JSON that haven't been modified in a while.

## How to use it

Start by exporting you Bitwarden vault to JSON.

Then run

    bitwarden_check.py /path/to/bitwarden_export_yyyymmddHHMMss.json | less

Anything in red—last modified more than 12 months ago—is a candidate to be updated.

## Follow-On Tasks

There are some other things you should consider doing at this time to improve your account security and online privacy:

* Delete the account if you no longer need it.
* Make sure you have good 2FA set up. Google Authenticator is preferred.
* Change to use an email alias.
* Remove unnecessary personal information.
* Add some account misinformation (e.g. wrong name, location, profile photo, etc).
* Make sure the Bitwarden entry is complete and up-to-date.
* Set the Bitwarden entry to Archive if you no longer use it.