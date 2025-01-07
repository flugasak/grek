"""
File: local_grek.py
Author: FlyOnTheWall

Description:
    A local version of the bot, for troubleshooting issues

Usage:
    This should be run as a Discord bot, preferably on a suitable service, and invited to the discord servers where it is to be used.

Dependencies:
    - discord.py
    - Python3
    - python-dotenv
    

Notes:
    - This is a discord bot, it requires a DISCORD_TOKEN
"""

import grekbot
import os
from dotenv import load_dotenv

# Parameters:
# 1. discord token
# 2. SQLite file
# 3. Panel URI
# 4. Panel Key

load_dotenv()

TOKEN = "NO MATTER" # os.getenv('DISCORD_TOKEN')
SQLITE_FILE = os.getenv('SQLITE_FILE')
PTERO_ENDPOINT = os.getenv('PTERO_ENDPOINT')
PTERO_APIKEY = os.getenv('PTERO_APIKEY')

grekbot = grekbot.grek(TOKEN,SQLITE_FILE,PTERO_ENDPOINT,PTERO_APIKEY)

print(grekbot.testptero())

"""
import requests

# Set the API endpoint and bearer token
api_endpoint = "https://dac.musca.fi/api/client"
bearer_token = "ptlc_NOXlvw9bJWhmkGCTeo2PVLgxwn8YG0YMF1OUaH75wC2"

# Set the headers
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Accept": "application/json"
}

# Make the API request
response = requests.get(api_endpoint, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Request was successful, process the response data
    data = response.json()
    print(data)
else:
    # Request failed, print the status code and error message
    print(f"Error: {response.status_code} - {response.text}")
"""