async def execute(client):
    client_connected = False
    print("Please wait...")
    await client.logout()
    print("Client sucsessfully logged out")
    return 2

if __name__ == "__main__":
    pass
