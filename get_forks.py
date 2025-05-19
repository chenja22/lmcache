import requests
import csv
import os
from dotenv import load_dotenv

load_dotenv()


# --- Settings ---
owner = "vllm-project"
repo = "vllm"
token = os.getenv("git_token")

headers = {"Authorization": f"token {token}"}

url = f"https://api.github.com/repos/{owner}/{repo}/forks"

fork_users = []
page = 1
while True:
    response = requests.get(url, headers=headers, params={"per_page": 100, "page": page})
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        break

    data = response.json()
    if not data:
        break

    for fork in data:
        user = fork["owner"]["login"]
        fork_users.append(user)

    page += 1

with open("fork_users_vllm.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Username"])
    for user in fork_users:
        writer.writerow([user])

print(f"Saved to fork_users_vllm.csv.")
