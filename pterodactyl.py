"""
File: pterodactyl.py
Author: FlyOnTheWall

Description:
    Handles the connections to the pterodactyl panel

Usage:
    Use through the Grek bot

Dependencies:
    

Notes:
    <Add any additional notes or information that might be useful for other developers.>
"""

# Imports
import requests
import json

# Class definitions

class pterodactyl:
    def __init__(self, endpoint, apikey):
        self.endpoint = endpoint
        self.apikey = apikey
    
    def get_data(self,tail):
        headers = {
            "Authorization": f"Bearer {self.apikey}",
            "Accept": "application/json"
        }
        endpoint = self.endpoint+tail
        response = requests.get(endpoint,headers=headers)
        print(f'[DEBUG] endpoint: {endpoint}')
        print(f'[DEBUG] Bearer: {self.apikey}')
        return response.json()

    def get_server_status(self):
        return self.get_data("")
        