import discord
import os
import random

IMGS = os.listdir("imgs")


class YeBot(discord.Client):
    async def on_ready(self):
        print(f"Logged successfully as {self.user}")

    async def on_message(self, message):
        if message.content.startswith('ye!img'):
            await message.channel.send(file=discord.File(f"imgs/{random.choice(IMGS)}"))


if __name__ == "__main__":
    ye = YeBot()
    ye.run(os.environ.get("DISCORD_API_TOKEN"))