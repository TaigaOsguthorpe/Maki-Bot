# Image dumper command line tool for Maki-Bot 5.0
##from tkinter import Tk
##from tkinter.filedialog import askopenfilenames
from aioconsole import ainput
from discord import File


async def execute(client):
    ##Tk().withdraw()
    ##filemanes = askopenfilenames()
    ##print(filemanes)
    while True:
        console_input = await ainput("Maki-Bot/dumper: Channel ID >> ")
        if console_input == "exit":
            return  # Returns nothing basically ending itself and returning to the main console input
        try:
            console_input = int(console_input)
        except ValueError:
            print("ValueError! Channel ID must be a base 10 integer")
            continue  # Makes it go back to the start of the loop

        channel = client.get_channel(console_input)
        print("Dumpping channel set to: {0}".format(channel.name))
        loop = 1
        files = []
        while True:

            console_input = await ainput("Maki-Bot/dumper: File >> ")
            #print(console_input)
            if console_input == "send":
                print("Files to send {0}".format(len(files)))
                sent = 0
                for f in files:
                    sent = sent +1
                    await channel.send(file=File(f))
                    print("Sent {0}/{1}".format(sent, len(files)))
                ##print("Sent!")

            if console_input == "exit":
                return
            else:
                files.append(console_input)


    #for image in filenames:
        #await channel.send('hello')
    ##channel.send('hello')
