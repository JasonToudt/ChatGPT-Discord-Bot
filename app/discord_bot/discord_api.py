from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

#Import environment variables in .env file
load_dotenv()

#Setting Discord token variable from .env file
discord_token = os.getenv('TOKEN')

#Creating methods for interacting with Discord
class MyClient(discord.Client):
    async def on_ready(self):                            #Method confirming bot is logged in and ready
        print("Successfully logged in as: ", self.user)

    async def on_message(self, message):                 #Method for bot to listen for messages from the client
        print(message.content)
        if message.author == self.user:                  #Check to see if message is from the bot itself, then return nothing if True
            return
        command, user_message= None, None

        for text in ['!ai','!bot','!gpt']:               #Listen for specific commands
            if message.content.startswith(text):
                command=message.content.split(' ')[0]
                user_message=message.content.replace(text, '')
                print(command, user_message)

        #Bot answer/response
        if command == '!ai' or command == '!bot' or command == '!gpt':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")

#Setting Discord Intents variable
intents = discord.Intents.default()
intents.message_content = True

#Creating an instance of the MyClient class, stored in variable "client"
client = MyClient(intents=intents)
