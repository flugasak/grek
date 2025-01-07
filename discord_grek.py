"""
File: discord_grek.py
Author: FlyOnTheWall

Description:
    A Discord bot that handles applications to join server allowlists. 

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
from discord.ext import commands
import os
from dotenv import load_dotenv

# Parameters:
# 1. discord token
# 2. SQLite file
# 3. Panel URI
# 4. Panel Key

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
SQLITE_FILE = os.getenv('SQLITE_FILE')
PTERO_ENDPOINT = os.getenv('PTERO_ENDPOINT')
PTERO_APIKEY = os.getenv('PTERO_APIKEY')

grek = grekbot.grek(TOKEN,SQLITE_FILE,PTERO_ENDPOINT,PTERO_APIKEY)
    

# Discord events
@grek.command(name='messmp',help='Generic MesSMP command',pass_context=True, no_pm=True)
async def messmp(ctx: commands.Context, *args):
    print('so far so good?')
    print(f'args: {args}')
    
    if args.__len__() > 0:
        await grek.grek_do(ctx, args)
    else:
        print("ARHG - no args")

# Finally ready to run!
grek.run()
