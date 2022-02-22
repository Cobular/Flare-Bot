from http import client
from nextcord import Interaction, Client, SlashOption
from webserver import app
import shelve
import atexit
from dataclasses import dataclass

client = Client()
my_shelf = shelve.open("./data_shelf")


@dataclass
class BotData:
    bot_id: int
    guild_id: int
    channel_id: int
    command: str


def exit_handler():
    my_shelf.close()


atexit.register(exit_handler)


@client.slash_command(name="Add bot", guild_ids=["272189051413725184"])
async def something(
    bot_id: SlashOption(name="Bot ID", required=True),
    command_str: SlashOption(name="Command to Invoke", required=True),
):
    bot_data = BotData(
        
    )
    my_shelf[bot_id] = "eee"

PORT = "8333"

client.loop.create_task(app.run_task("localhost", PORT))

client.run("OTQ0MzQ1NDY5MTI2MDY2MjQw.YhAQQA.SmqEBwmSoUBQbq5QcdMO8V3ZcRA")
