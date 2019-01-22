from os import system
from sys import platform
async def execute(*args, **kwargs):
    """Clears the console with the aproprit os shell call.
    This command should only be run by the bots main thread only!"""
    if platform == "linux":
        system('clear')  # System calls the shell
    elif platform == "win32":
        system('cls')

if __name__ == "__main__":
    exit()
