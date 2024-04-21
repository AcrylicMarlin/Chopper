import asyncio

import discord

from chopper import Chopper


intents=discord.Intents.all()
status=discord.Status.online
activity = discord.Activity(name = 'One Piece!', type = discord.ActivityType.streaming, url = 'https://www.youtube.com/watch?v=o-YBDTqX_ZU')


client = Chopper(intents=intents, status=status, activity=activity)

if __name__ == "__main__":
    asyncio.run(client.run())
