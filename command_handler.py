# Imports
import discord
from discord import Intents, Client, Message
from discord.ext import commands
from discord.ui import View, Button

# Functions
## Applications
## Moderation
## Information
# Handlers / Views
## Application
## Moderation
## Information


# Functions
## Applications

async def requestApplication(ctx: commands.Context):
    grekLogContext(ctx)

## Information

def grekLog(message: str):
    print(f'{message}')

def grekLogContext(ctx: commands.Context):
    # Logging
    username: str = str(ctx.author)
    user_message: str = ctx.message
    channel: str = str(ctx.channel)
    print(f'[{channel}] {username}: "{user_message}"')

# Handlers / Views
## Application

class grekDo():
    def __init__(self):
        pass

class grekApplicationView(View):
    def __init__(self, ctx, timeout = 180):
        super().__init__()
        self.ctx = ctx

        self.add_item(grekApplicationServerList())

    
    @discord.ui.button(label="Apply")
    async def applyButton(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("You have chosen to apply to a server.",ephemeral=True)

    @discord.ui.button(label='Cancel')
    async def cancelApplyButton(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("Application cancelled.",ephemeral=True)

class grekApplicationServerList(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="MesSMP S1",description="The old S1 server"),
            discord.SelectOption(label="Warped Shores",description="The current public MesSMP server"),
            discord.SelectOption(label="Public MesSMP S2",description="The new, upcoming MesSMP project"),
            discord.SelectOption(label="MinecraftBuddies",description="Alex's domain")
        ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"Your choice is {self.values[0]}!",ephemeral=True)
