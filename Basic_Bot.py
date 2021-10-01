import discord
import os
from keep_bot_alive import keep_alive


client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in a {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('Hi bot') or message.content.startswith('Hi'):
        await message.channel.send('Hello')
    if message.content.startswith('Tell me about you'):
        await message.channel.send('I am Basic Bot made for discord servers using Python programming language. Click in the bot icon and see discrption to know know more ')
    if message.content.startswith('What can i do on this server?'):
        await message.channel.send('You can test bots made by you. Go to https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXdFM2lZN0dQN0M1OXZOQ0Y3T2pCenBidlpNQXxBQ3Jtc0tuMzNOWG92WmZBQWRWWmd2MzJoQlpQWVF3U29vUkRyNnM5WXllVndKOXJZNi1UVG1GbmI2TGJlM3A0WTB0bk1rUmNHby1zRF9fTmJ4QzdwcDBWQl92QnY2ekxqWExZVzZKRUx5T2taOWUyMXpudmtFQQ&q=https%3A%2F%2Fdiscord.com%2Fdevelopers%2Fapplications to get started ')
    
    
osenv=os.getenv('OS')
print('TOKEN=',osenv)

keep_alive()
client.run(osenv)

