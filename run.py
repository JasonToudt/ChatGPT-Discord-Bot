#Import packages from discord_bot directory
from app.discord_bot.discord_api import client, discord_token

#Run class object, and pass discord_token to initiate the bot connection
#Checks whether the code is being run as the main program, and not being imported as a module
if __name__ == '__main__':
    client.run(discord_token)
