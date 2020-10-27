from discord.ext import commands
from sources.api import wikipedia_api as Wiki

# TODO: Add picture return function

class Wikipedia(commands.Cog, name='Wikipedia'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="getArticle")
    async def getArticle(self, ctx, arg):
        """Get an Wikipedia article
        use: !getArticle \"Dutch East India Company\""""

        result = Wiki.get_summary(arg)

        await ctx.send(result)


def setup(bot):
    bot.add_cog(Wikipedia(bot))
