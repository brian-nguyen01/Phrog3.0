import os
import discord
import res
import sound_handler
import command_handler
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

    
async def send_message(message, user_message, is_priv):
    try:
        response = res.handle_res(user_message)
        await message.author.send(response) if is_priv else await message.channel.send(response)
    except Exception as e:
        print("No reponse has been found")
        print(e)
        
        
def run_discord_bot():
    TOKEN = os.getenv('MYTOKEN')
    
    intents = discord.Intents.default()
    intents.message_content = True
    # client = discord.Client(intents=intents)
    client = commands.Bot(command_prefix='?', intents=intents)
    @client.event
    async def on_ready():
        print(f'Logged on as {client.user}!')
        
    @client.event
    async def on_message(message):
        user_message = str(message.content)
        print(f'Message from {message.author}: {user_message}')
        if message.author != client.user:
            if user_message[0] == '!':
                user_message = user_message[1:]
                await send_message(message, user_message, is_priv=True)
            # elif user_message[0] == '?':
            #     user_message = user_message[1:]
            #     await command(user_message)
            else:
                await send_message(message, user_message, is_priv=False)
                
    @client.command()
    async def join(ctx):
        try:
            channel = ctx.author.voice.channel
            voice_client = await channel.connect()
        except Exception as e:
            print(e)
        
    client.run(TOKEN)