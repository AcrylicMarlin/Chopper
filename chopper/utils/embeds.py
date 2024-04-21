import discord


class WelcomeEmbed(discord.Embed):
    def __init__(self, member:discord.Member, bot:discord.Client):
        super().__init__(title="Welcome!", description=f"Welcome {member.mention} to {member.guild.name}!")
        self.set_thumbnail(url=member.avatar_url)
        welcome_image = discord.File("./welcome_image.png", filename="welcome_image.png")
        self.set_image(url="attachment://welcome_image.png")
        self.set_footer(text=f"Chopper", icon_url=bot.user.avatar_url)