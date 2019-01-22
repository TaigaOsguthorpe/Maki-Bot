#Maki Nishikino Bot (西木野真姫)
import sys
import os
import subprocess
import asyncio
import discord
import logging
import bot_token
import STATICS
from console_commands import ccmd_help, ccmd_clear, ccmd_info, ccmd_image_dumper, ccmd_exit, ccmd_restart
from user_commands import cmd_catgirl
from aioconsole import ainput
import atexit
#from aiohttp import ClientSession as aiohttpSession


client = discord.Client()
embed = discord.Embed

##    Set up Client logging    ##
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

prefix = STATICS.PREFIX


##     Console     ##
console_commands = {
    # Image dumper
    "dumper": ccmd_image_dumper,
    "d": ccmd_image_dumper,
    "help": ccmd_help,
    "h": ccmd_help,
    "clear": ccmd_clear,
    "cls": ccmd_clear,
    "info": ccmd_info,
    "exit": ccmd_exit,
    "quit": ccmd_exit,
    "restart": ccmd_restart
}


quit_flag = False
restart_flag = False


async def console_input_handler():
    while True:
        console_input = await ainput("Maki-Bot >>> ")
        #print(console_input)
        if console_commands.__contains__(console_input):
            info = await console_commands.get(console_input).execute(client)  # Gets the command specified and runs the key with the arg client
            if info is 1:
                global quit_flag
                quit_flag = True
                return

            elif info is 2:
                global restart_flag
                restart_flag = True
                return

        else:
            print("{0} Is not a valid command. Tpye help for commands".format(console_input))
    sys.exit()

#dir_path = "{0}/{1}".format(os.path.dirname(os.path.realpath(__file__)), __file__)

def exit_handler():
    """Handels exiting the program"""
    #print("succ")
    if client.loop.is_running():
        """First to check that the asyncio event loop (client.loop) is still running"""
        print("Warning! Client event loops is still running!")
        try:
            loop.stop()
        except Exception:
            raise

    if quit_flag is True:
        print("Normal Shutdown")

    elif restart_flag is True:
        print("Maki-Bot restarting...")
        subprocess.Popen([sys.executable, "main.py"])

    else:
        print("Warning! Unknown exit!")
    #print("Please, no! Senpai!! D:")




##     Discord     ##


@client.event
async def on_connect():
    #client.loop.Task.cancel()
    print("Bot is logged in successfully but NOT fully operational")


@client.event
async def on_ready():
    """"Event Called by discord.py when the bot is ready."""
    print("Bot is fully operational")
    print("----------------------------------------------------------------------------")
    print(" Running On Severs:\n")
    [(lambda s: print(" - {0} - ({1})".format(s.name, s.id)))(s) for s in client.guilds]
    print("\n - Running in - {0} Guilds/Servers".format(len(client.guilds)))
    print("----------------------------------------------------------------------------")
    game = discord.Game("Game Name")
    stream = discord.Streaming(url="https://www.twitch.tv/channel", name="Title Name")
    client.loop.create_task(console_input_handler())  # registers the console_input_handler
    await client.change_presence(status=discord.Status.online, activity=game)

#     Commands     ##
user_commands = {
    "catgirl": cmd_catgirl
}

@client.event
async def on_message(message):
    if message.content.startswith(prefix):
        if message.author.bot:
            print("Bot detected!!")

        invoke = message.content.lower()[len(prefix):].split(" ")[0]  # Basically split after prefix and after first word  "!<---help--->"
        args_out = message.content.lower().split(" ")[1:]  # Split at a space "-catgirl random" --> "random"
        if user_commands.__contains__(invoke):
            await user_commands.get(invoke).execute(client, message, args_out, embed)#, aiohttpSession)
    #print(message.content)


atexit.register(exit_handler)
print("logging in")
client.run(bot_token.token)
