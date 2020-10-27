from discord.ext import commands


class Voice(commands.Cog, name="Vocie"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='voicetest')
    async def cool_bot(self, ctx):
        """Vocie test function"""
        await ctx.send(f'Voice is working')


def setup(bot):
    bot.add_cog(Voice(bot))