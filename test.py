import discord
import bot_token
import time
import sys
import subprocess
import os
from aioconsole import ainput

flag = False

class Maki(discord.Client):
    restart = False

    async def console_input(self):
        while True:
            console_input = await ainput("Maki-Bot >>> ")
            if console_input == "restart":
                self.restart = True
                await self.close()
            elif console_input == "quit":
                self.restart = False
                await self.close()
            else:
                pass




#    @client.event
    async def on_connect(self):
        print("Bot connected")


#    @client.event
    async def on_ready(self):
        print("Bot fully operational")
        print("starting console input")
        self.loop.create_task(self.console_input())


    async def on_message(self, message):
        #print("Message: {0}".format(message))
        print("message got")
        #await self.logout()
        #print("logged out")
        print(message.content)


    """def start(self):
        self.client.run(bot_token.token)"""

if __name__ == "__main__":
    print("starting")
    maki = Maki()
    maki.run(bot_token.token)
    print("ended self?")
    print(maki.restart)
    if maki.restart is False:
        sys.exit()
    else:
        print("else")
        os.execl(sys.executable, sys.executable, *sys.argv)
        #subprocess.Popen([sys.executable, "test.py"])
        print("restarted")
        sys.exit()
