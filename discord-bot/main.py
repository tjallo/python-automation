# Depenedencies
from discord.ext import commands

# Local imports
from resources import secret, config

startup_extensions = ["sources.commands.chat"]

bot = commands.Bot(command_prefix=config.prefix, description="Hello world!")


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(secret.BOT_TOKEN)