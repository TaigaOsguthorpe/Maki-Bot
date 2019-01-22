async def execute(client, **kwargs):
    print("Please wait...")
    await client.logout()
    print("Client sucsessfully logged out")
    return 1

if __name__ == "__main__":
    pass
