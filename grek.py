"""
File: grek.py
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

## Imports
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, errors, app_commands
from discord.ext import commands
from responses import get_response
import command_handler
import db_manager
import pterodactyl

## Load the token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SQLITE_FILE = os.getenv('SQLITE_FILE')
PTERO_ENDPOINT = os.getenv('PTERO_ENDPOINT')
PTERO_APIKEY = os.getenv('PTERO_APIKEY')

## Set up the bot with intents
intents = Intents.default()
intents.message_content = True
#intents.messages = True
#intents.members = True
bot = commands.Bot(intents=intents,command_prefix='!')


## Handling startup

### Database handler
db_handler = db_manager.grekData(SQLITE_FILE)

### Pterodactyl handler
ptero = pterodactyl.pterodactyl(PTERO_ENDPOINT, PTERO_APIKEY)

### Bot Edition
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


## Commands

# Start a new application
@bot.command(name='apply',help='Apply for access to a game server')
async def grek_start_application(ctx: commands.Context):
    view = command_handler.grekApplicationView(ctx)
    await ctx.send("Application to join a server", view=view)

# A generic MesSMP command, with subcommands
@bot.command(name='messmp',help='Generic MesSMP command',pass_context=True, no_pm=True)
@app_commands.describe(
    option='What would your like to MesS up today?'
)
async def grek_do_messmp(ctx: commands.Context, command, *args):
    # await ctx.send('Generic MeSSMP command dooblydoo')
     
    match command:
        case 'ptero':
            await ctx.send('Attempting to call dac..')
            output = ptero.get_server_status()
            await ctx.send(f'Output: {output}')
        case 'server':
            match args[0]:
                case 'list':
                    servers = db_handler.list_servers()
                    list = f"Servers currently managed: {servers.__len__()}\n"
                    if list.__len__ == 0:
                        await ctx.send(f'Could list some servers.. If I had any.')
                    else:
                        for server in servers:
                            list += f"- *ID: {server[0]}* **{server[1]}:** {server[2]}\n"
                        await ctx.send(f'{list}')
                case 'add':
                    try:
                        db_handler.add_server(args)
                    except:
                        await ctx.send(f'Servers need a name and a description.')
                        return
                    await ctx.send(f'{ctx.author} added {args[1]}')
                case 'remove':
                    try:
                        db_handler.del_server(args)
                    except:
                        await ctx.send(f'I\'m going to need an ID for the server you want to remove.')
                        return
                    await ctx.send(f'{ctx.author} removed {args[1]}')
                case _:
                    await ctx.send('What did you want me to do with the servers again..?')

        case 'allowlist':
            await ctx.send(f'I\'m the (allowlist) supervisor.')
        case '':
            return
        case _:
            await ctx.send(f'I\'m sorry, Dave. {command} P1 {args[0]}')

## Main Entry Point - This is when we run stuff after defining it all
def main() -> None:
    try:
      bot.run(TOKEN)
    except errors.PrivilegedIntentsRequired as e:
        print(e)
    except errors.ConnectionClosed as e:
        print(e)

if __name__ == '__main__':
    main()

