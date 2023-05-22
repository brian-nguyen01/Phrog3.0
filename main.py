# import os
# import discord
# from dotenv import load_dotenv
# from discord.ext import commands

# intents = discord.Intents.default()
# intents.message_content = True
# load_dotenv()


# TOKEN = os.getenv('MYTOKEN')
# class MyClient(discord.Client):
#     async def on_ready(self):
#         print(f'Logged on as {self.user}!')

#     async def on_message(self, message):
#         print(f'Message from {message.author}: {message.content}')
        
#     async def greet(ctx, name):
#         await ctx.send(f'Hello, {name}!')
        
        
        
        

# client = MyClient(intents=intents)
# client.run(TOKEN)

import bot


bot.run_discord_bot()

