from discord.ext import commands
from discord import FFmpegOpusAudio
from discord.utils import get
import subprocess, asyncio


def getTimeFromFile(file):
    args=("ffprobe","-show_entries", "format=duration","-i",file)
    popen = subprocess.Popen(args, stdout = subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read().decode().split()[1]

    time = float(output.split('=')[-1])

    return time


async def disconnectFromChannelAfterNSeconds(voice, N):
    await asyncio.sleep(N)
    await voice.disconnect()


class Voice(commands.Cog, name="Voice"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='chevyvan')
    async def chevyvan(self, ctx):
        """Only for real men
        use: !chevyvan
        """

        file = 'resources/sounds/chevyvan.mp3'
        await ctx.send('If you wanna be a real man')

        channel = ctx.message.author.voice.channel
        if not channel:
            await ctx.send("You are not connected to a voice channel")
            return
        voice = get(self.bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.move_to(channel)
        else:
            voice = await channel.connect()
        source = FFmpegOpusAudio(file)
        player = voice.play(source)

        runtime = getTimeFromFile(file)

        await disconnectFromChannelAfterNSeconds(voice, runtime + 2)


        


def setup(bot):
    bot.add_cog(Voice(bot))
