# Depenedencies
import os
from discord.ext import commands

# Local imports
from resources import secret, config

startup_extensions = [f"sources.commands.{x[:-3]}" for x in os.listdir(os.getcwd() + "\\sources\\commands") if x[-3:] == ".py"]

bot = commands.Bot(command_prefix=config.prefix, description=config.description)

# Startup message
@bot.event
async def on_ready():
    print("Bot has started up...")
    print('We have logged in as {0.user}'.format(bot))

if __name__ == "__main__":
    loaded_ext = []
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
            loaded_ext.append(extension.split(".")[-1])
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    print("Loaded the following extensions: " + ", ".join(loaded_ext))

    bot.run(secret.BOT_TOKEN)
