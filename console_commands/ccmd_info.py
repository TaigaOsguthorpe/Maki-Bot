async def execute(client):
    print("----------------------------------------------------------------------------")
    print("Running On Severs:\n")
    [(lambda s: print(" - {0} - ({1})".format(s.name, s.id)))(s) for s in client.guilds]
    print("\n - Running in - {0} Guilds/Servers".format(len(client.guilds)))
    print("----------------------------------------------------------------------------")

if __name__ == "__main__":
    exit()
