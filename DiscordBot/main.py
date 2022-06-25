
import discord
import json

TOKEN_FILE = open("DiscordBot/token.txt", 'r')
TOKEN = TOKEN_FILE.readline()
TOKEN_FILE.close()

msgs_array = []

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, msg):
        if msg.channel.name == "chat-with-bot":
            print('{0.content}'.format(msg))

            with open("DiscordBot/messages.json", 'r') as file:
                msgs_array = json.load(file)

            msgs_array.append('{0.content}'.format(msg))

            with open("DiscordBot/messages.json", 'w') as file:
                json.dump(msgs_array, file, indent=4)

client = MyClient()
client.run(TOKEN)

