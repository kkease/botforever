import discord
import openai
import os
from discord.ext import commands
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY

# Set up the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ask(ctx, *, question):
    """Ask ChatGPT a question."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful assistant."},
                      {"role": "user", "content": question}]
        )
        answer = response["choices"][0]["message"]["content"]
        await ctx.send(answer)
    except Exception as e:
        await ctx.send("Error: Unable to process request.")
        print(e)

# Run the bot
bot.run(DISCORD_TOKEN)
