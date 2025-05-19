import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("git_token")

headers = {
    "Authorization": f"token {token}"
}

def get_user_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [
            username,
            data.get("name", ""),
            data.get("email", ""),
            data.get("company", ""),
            data.get("blog", "")
        ]
    else:
        return [username, "", "", "", ""]

# Read usernames
with open("fork_users_vllm.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    usernames = [row[0] for row in reader]

rows = [["Username", "Name", "Email", "Company", "Blog/Website"]]
for username in usernames:
    rows.append(get_user_data(username))

with open("fork_users_vllm_enriched.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

print("Saved to fork_users_vllm_enriched.csv.")
