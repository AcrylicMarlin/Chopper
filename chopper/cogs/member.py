from discord.ext import commands
import discord


class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, id=1225527101357162587)
        if channel is None:
            return
        await channel.send(f"Welcome {member.mention} to {member.guild.name}!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, id = 1225527101357162590)
        if channel is None:
            return
        await channel.send(f"Goodbye {member.mention} from {member.guild.name}!")