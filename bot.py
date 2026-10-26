#region start
"""
Slash commands, views, buttons. Thin: it calls quiz.py and displays results
"""
#endregion

# import logging
# import traceback

import discord
from discord import app_commands  # noqa: F401
from discord.ext import commands

# from main import TEST_SERVER as SERVER


class Client(commands.Bot):

    async def setup_hook(self):
        guild = discord.Object(id=self.guild_id)
        self.tree.copy_global_to(guild=guild)
        synced = await self.tree.sync(guild=guild)
        print(f"Synced {len(synced)} commands to guild {guild.id}")


    async def on_ready(self):
        print(f"Logged in as {self.user}! Quack!!")

        # except Exception as e:
        #     print(f'Error syncing commands: {e}')
        #     error_log = traceback.format_exc()
        #     print("--- LOG START --- ")
        #     print(error_log)
        #     print("--- LOG END --- ")
            
            # logger = logging.exception("Failed to execute do_something")
            # logger.info("Foobar")

            # logger = logging.getLogger(__name__)
            # logger.info("Foobar")
            # raise

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == self.user:
            return
        
        if message.content.startswith('quack'):
            await message.channel.send(f'Quack quack! Quack {message.author}')
    
    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('Quack!!')

class DifficultyButton(discord.ui.Button):
    def __init__(self, difficulty):
        super().__init__(label=difficulty["label"], style=difficulty["style"], emoji=difficulty["emoji"])
        self.difficulty = difficulty["label"]

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Starting a {self.difficulty} quiz!")

intents = discord.Intents.default()
intents.message_content = True 
client = Client(command_prefix="/", intents=intents)

""" /help """
@client.tree.command(name="help", description="View a list of supported commands")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message("Help")

""" /quiz """
@client.tree.command(name="quiz", description="Start a quiz")
async def quiz(interaction: discord.Interaction):
    await interaction.response.send_message("Starting the quiz...")

    # if difficulty == None:
    #     print("No difficulty found, prompting the user to select...")
    #     prompt_difficulty(interaction)

    # if category == None:
    #     print("No category found, prompting the user to select...")
    #     prompt_category(interaction)

    

async def prompt_category(interaction: discord.Interaction):
    # categories = ['Git', 'CLI', 'Python']
    # for category in categories:
    pass

async def prompt_difficulty(interaction: discord.Interaction):
    difficulties = [
        {
            'label': 'easy',
            'style': discord.ButtonStyle.green,
            'emoji': '🟢'
        },
        {
            'label': 'medium',
            'style': discord.ButtonStyle.blurple,
            'emoji': '🟣'
        },
        {
            'label': 'hard',
            'style': discord.ButtonStyle.red,
            'emoji': '🔴'
        }
    ]

    difficulty_view = discord.ui.View()
    for difficulty in difficulties:
        difficulty_view.add_item(DifficultyButton(difficulty))

    await interaction.response.send_message("Pick a difficulty:", view=difficulty_view)

""" /rankings """
@client.tree.command(name="highscores", description="View the high scores within the server")
async def view_highscores(interaction: discord.Interaction):
    await interaction.response.send_message("High scores")

""" /review """
""" /board """
""" /explain """
""" /quack """

""" /about """
@client.tree.command(name="about", description="Learn more about Professor Quack.py")
async def view_about(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Hello, I am Professor Quack", 
        url="https://github.com/oswwwaldo/professor-quack-py", 
        description="I am a talking duck on Discord, I was born on October 25th 2026 and my favorite color is yellow. What else could you possibly want from this description? Go answer some coding challenges!", 
        color=discord.Color.green())
    embed.set_author(name="This bot is a open source repository!", url="https://github.com/oswwwaldo/professor-quack-py", icon_url="https://i.pinimg.com/736x/16/61/78/1661781e600a5342ae9288c7bc6b15d7.jpg")
    embed.set_thumbnail(url="https://i.pinimg.com/736x/6a/bf/bb/6abfbbb052f77a936a5b0af80c118543.jpg")
    embed.add_field(name="Server Name", value={interaction.guild.name}, inline=True)
    embed.add_field(name="Server ID", value={interaction.guild.id}, inline=True)
    embed.add_field(name="Author", value="Oswaldo De Los Santos (github.com/oswwwaldo)", inline=False)
    embed.set_footer(text="quack quack quack")
    await interaction.response.send_message(embed = embed)



def run_bot(token, guild_id):
    client.guild_id = guild_id
    client.run(token)