"""
File: grekbot.py
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
import discord
from discord.ext import commands
from responses import get_response
import command_handler
import db_manager
import pterodactyl

class grek(commands.Bot):
    def __init__(self,token,sqlitedb,panel_uri,panel_apikey):
        # Config
        self.discord_token = token
        self.sqlite_file = sqlitedb
        self.panel_endpoint = panel_uri
        self.panel_apikey = panel_apikey
        self.ptero = pterodactyl.pterodactyl(self.panel_endpoint, self.panel_apikey)
        self.db = db_manager.grekData(self.sqlite_file)

        ## Set up the Bot config
        self.Botcommand_prefix = '!'
        self.Botintents = discord.Intents.default()
        self.Botintents.message_content = True
        #self.intents.messages = True
        #self.intents.members = True
        
        ## Run the super init
        super().__init__(command_prefix=self.Botcommand_prefix,intents=self.Botintents)
        
    async def on_ready(self):
        print(f'{self.user.name} is ready to fight!')

    
    def test(self):
        print("Grek feel good!")

    def testptero(self):
        return self.ptero.get_server_status()
        
    def run(self):
        super().run(self.discord_token)

    async def grek_do(self, ctx: commands.Context,args):
        
        # Which command are we doing?
        match args[0]:
            case 'ptero':
                print('ptero do')
                try:
                    await self.ptero_do(ctx, args[1:])
                except IndexError as e:
                    print(e)
                    await ctx.send_help()
                
            case 'server':
                print('server do')
            case _:
                print('what do')

    async def ptero_do(self, ctx: commands.Context, args):

        # What are we doing with the panels?
        match args[0]:
            case 'add':
                print('adding panel')
                await self.ptero_add_panel(ctx, args[1:])
            case 'remove':
                print('removing panel')
            case 'list':
                print('listing panels')

    async def ptero_add_panel(self, ctx: commands.Context, args):
        view = NewPanelView()
        await ctx.send("Add a new panel",view=view)
        await view.wait()
        if view.option:
            await ctx.send(f"You entered {view.option}")
        else:
            await ctx.send("No option entered")

class NewPanelView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.option = None
    
    @discord.ui.TextInput(label="Option", custom_id="option_input")
    async def option_input(self, text_input: discord.ui.TextInput, interaction: discord.Interaction):
        self.option = text_input.value
        await interaction.response.defer()

    @discord.ui.Button(label="Submit", style=discord.ButtonStyle.green, custom_id="submit_button")
    async def submit_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.defer()
        self.stop()