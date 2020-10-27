from discord.ext import commands


class Voice(commands.Cog, name="Voice"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='voicetest')
    async def voicetest(self, ctx):
        """Vocie test function, placeholder for now"""
        await ctx.send(f'Voice is working (this is still a placeholder)')


def setup(bot):
    bot.add_cog(Voice(bot))
