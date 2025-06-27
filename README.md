# Bitwarden Check

## Description

Shows entries in a Bitwarden export JSON that haven't been modified in a while.

## How to use it

Start by exporting you Bitwarden vault to JSON.

Then run

    bitwarden_check.py /path/to/bitwarden_export_yyyymmddHHMMss.json | less

Anything in red—last modified more than 12 months ago—is a candidate to be updated.

## Account maintenance

Do these to improve your account security and online privacy:

* Delete the account if you no longer need it.
* Update the password if it has been found in breach data, is not strong enough, or is old.
* Make sure you have good 2FA set up. Google Authenticator is preferred.
* Use an email alias instead of your real email. (Not recommended for financial, government, or any other important accounts).
* Remove unnecessary personal information.
* Add some account misinformation (e.g. wrong name, location, profile photo, etc).
* Make sure the Bitwarden entry is complete and up-to-date.
* Set the folder to Archived if you no longer use it.
