#import json
from secrets import choice
from user_commands import kittys
#from requests import get
#from discord import Embed

async def execute(client, message, args_out, embed, **kargs):
    #print(args_out)
    if len(args_out) > 0:

        if args_out == ['lewd']:
            #print("lewd")
            em = embed(title='Lewd Catgirl:', colour=0xfc59ff)
            url = choice(kittys.lewd_cats)
            em.set_image(url=url)
            await message.channel.send(embed=em)
            return

        if args_out == ['lewd', 'yuri']:
            #print("lewd yuri")
            em = embed(title='Lewd Yuri Catgirl:', colour=0xfc59ff)
            url = choice(kittys.lewd_cats_yuri)
            em.set_image(url=url)
            await message.channel.send(embed=em)
            return

        if args_out == ['nude']:
            #print("nude")
            em = embed(title='Nude Catgirl:', colour=0xfc59ff)
            url = choice(kittys.nude_cats)
            em.set_image(url=url)
            await message.channel.send(embed=em)
            await message.channel.send(nude)
            return
    else:
        em = embed(title='Catgirl:', colour=0xfc59ff)
        url = choice(kittys.cats)
        em.set_image(url=url)
        await message.channel.send(embed=em)
        return


"""    with aiohttpSession() as session:
        print("Made session")
        async with session.get('https://nekos.life/api/v2/img/neko') as r:
            print(r.status)
            if r.status == 200:
                js = await r.json()
                await message.channel.send(js['url'])
                return
                #print(json.dumps(js, indent=4, sort_keys=True))
"""
