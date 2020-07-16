import json

accounts = []

print("Reading exported JSON...")
with open("bitwarden-export.json", "r", encoding="utf8") as export_file:
    vault = json.load(export_file)
    vault = vault["items"]

    for item in vault:
        if item["type"] == 1:
            if item["login"]["totp"]:
                accounts.append((item['name'], item['login']['username']))

print("Transfer the following accounts:")
for account in accounts:
    print("{} - {}".format(account[0], account[1]))

print("Regeneration of TOTP strongly recommended!")