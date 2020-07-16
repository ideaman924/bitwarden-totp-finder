# bitwarden-totp-finder

Used to find accounts utilizing TOTP tokens in your vault.

## Why?

My Bitwarden Premium subscription was expiring and I'm too poor to pay for another year. I thought I'd use the opportunity to transfer all of my TOTP codes to a proper authenticator that is separate from my password manager.

## Usage

Export your vault in JSON format.

Rename the file to `bitwarden-export.json` and place it in the same directory as the `main.py` script. Run and see which accounts you need to migrate!