from discord.ext import commands
import discord

from sources.api import image_api as Img

class Images(commands.Cog, name ="Images"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="imgSearch")
    async def imgSearch(self, ctx, arg):
        """
        Search DuckDuckGo for images (takes a little while to load)
        use: !imgSearch "The Spanish Inquisition"
        """
        await ctx.send("Processing...")

        link = Img.getImageLink(arg)

        await ctx.send(link)

    @commands.command(name="deepfry")
    async def fileDownload(self, ctx, arg):
        """
        deepfry images from the internet
        use: !deepfry "Jan Pieterszoon Coen"
        """

        await ctx.send(f"Working on deepfrying {arg}....")

        path = await Img.deepfrySearch(arg)
        await ctx.send(file=discord.File(path))

def setup(bot):
    bot.add_cog(Images(bot))

