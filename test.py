import json
def read_accounts():
    with open("accounts.json", "r") as file:
        return json.load(file)
read_accounts()