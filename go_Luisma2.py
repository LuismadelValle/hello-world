from telethon import TelegramClient, events, connection
import time
import random
import asyncio
import re
import time
from random import uniform

on = True
advisers = ['lvl.1 Jaeger', 'lvl.1 Strategist']
lvl = 1


state = False

loop = asyncio.get_event_loop()

api_id = 1384047
api_hash = 'ff7833fe3651498aa36eb6f6212f3d6a'
phone='LuismaPhone'
client=TelegramClient(phone,api_id,api_hash, connection = connection.ConnectionTcpMTProxyRandomizedIntermediate, proxy = ('proxy.digitalresistance.dog', 443, 'd41d8cd98f00b204e9800998ecf8427e'))

client.start()

api_id = 2518284
api_hash = '8651bad3d3e21d7267a5ee988809ae47'
phone='EnzoPhone'
client2=TelegramClient(phone,api_id,api_hash, connection = connection.ConnectionTcpMTProxyRandomizedIntermediate, proxy = ('proxy.digitalresistance.dog', 443, 'd41d8cd98f00b204e9800998ecf8427e'))

client2.start()

api_id = 1385527
api_hash = 'af589b5f7cbd78365c4e0ee3d48e1406'
phone='Dayana'
client3=TelegramClient(phone,api_id,api_hash, connection = connection.ConnectionTcpMTProxyRandomizedIntermediate, proxy = ('proxy.digitalresistance.dog', 443, 'd41d8cd98f00b204e9800998ecf8427e'))

client3.start()

@client.on(events.NewMessage(chats=('chtwrsbot'), incoming = True))
async def my_event_handler(event):
    global state
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        time.sleep(random.randint(30, 60))
        #await client.send_message('chtwrsbot', '/go')
        buttons = await event.get_buttons()
        for bline in buttons:
            for button in bline:
                if 'Intervene' in button.button.text:
                    await button.click()
    #if 'To accept their offer, you shall' in event.raw_text:
        #time.sleep(random.randint(30, 50))
        #await client.send_message('chtwrsbot', '/pledge')
    if 'has ordered Steel mold' in event.raw_text:
        await client.forward_messages(-1001467982915, event.message)
    if on and 'Advisers available for hire' in event.raw_text:
        lines = event.raw_text.splitlines()
        link = None
        gold = 999999
        link_re = re.compile('(/adv_\w{4})')
        gold_re = re.compile('(\d{3})')
        for line in lines:
            for adv in advisers:
                if adv in line:
                    act_link = link_re.search(line).group()
                    act_gold = int(gold_re.search(line).group()) 
                    if gold > act_gold:
                        link = act_link
                        gold = act_gold
        if link is not None:
            await asyncio.sleep(0.15)
            await client.send_message('chtwrsbot', link)
    elif on and 'Hire: /g_hire' in event.raw_text:
        link = re.search('(/g_hire \w{4})', event.raw_text).group()
        await asyncio.sleep(0.15)
        await client.send_message('chtwrsbot', link)
    elif '/g_pay' in event.raw_text:
        state = True
        lines = event.raw_text.splitlines()
        for line in lines:
            time.sleep(uniform(8,12))
            link = re.search('/g_pay \w{4}', line).group()
            await client.send_message('chtwrsbot', link)   
    elif state and 'invalid action' in event.raw_text:
        state = False
        await client.send_message(-1001467982915, '@HhH_Cuba Hectorrrrrrrrrrrrrrr falta money pon la pasta que falta y que el ninja que no pago te pague despues')
    elif 'Successfully funded!' in event.raw_text:
        await client.forward_messages(-1001467982915, event.message)
            

@client.on(events.NewMessage(chats=(728204488)))
async def my_event_handler(event):
    global on
    global adviser
    global lvl
    m = re.search('([a-zA-Z]+) lvl (\d)', event.raw_text)
    if m is not None:
        on = True
        adviser1, _, adviser2 = m.groups()
        adviser1 = 'lvl.%s %s' %(lvl, adviser1.capitalize())
        advicer2 = 'lvl.%s %s' %(lvl, adviser2.capitalize())
        advisers = [adviser1, adviser2]
    elif 'off' in event.raw_text:
        on = False
    elif 'on' in event.raw_text:
        on = True
    if '/ping' in event.raw_text:
        await client.send_message(728204488, 'pong')
    if '/myshop_open' in event.raw_text:
        time.sleep(uniform(15,58))
        await client.send_message('chtwrsbot', '/myshop_open')
    if '/advlist' in event.raw_text:
        time.sleep(60.1)
        await client.send_message('chtwrsbot', '/advlist')

@client.on(events.NewMessage(chats=(-1001467982915)))
async def my_event_handler(event):
    if 'g_pay' in event.raw_text:
        await client.send_message('chtwrsbot', event.raw_text)
    #if '[invalid action]' in event.raw_text:
        #await client.send_message(-1001467982915, '@HhH_cuba Hectoooooooooooooor falta money')
    if '/ping' in event.raw_text:
        await client.send_message(-1001467982915, 'pong de los cojones')

#@client.on(events.NewMessage(chats=(1475153683)))
#async def my_event_handler(event):
    #mensaje = event.raw_text.lower()
    #if 'luisma' in mensaje:
        #await client.send_message(1475153683, 'Los leo. Dejen de hablar de mi :P')

#@client.on(events.NewMessage(chats=(-1001494642874)))
#async def my_event_handler(event):
    #mensaje = event.raw_text.lower()
    #if 'luisma' in mensaje:
        #await client.send_message(-1001494642874, 'Los leo. Dejen de hablar de mi :P')
    #if 'Pole' in mensaje:
        #await client.send_message(-1001494642874, "#fermos")

#@client.on(events.NewMessage(chats=()))
#async def my_event_handler(event):
    #camara = event.raw_text.lower()
    #if 'camara' in camara:
        #me.send_message("me", message.chat.id)

@client.on(events.NewMessage(chats=(-1001476815468)))
async def my_event_handler(event):
    if '⚔️🐺' in event.raw_text:
        await client.forward_messages(698038449, event.message)
    if '⚔️🌑' in event.raw_text:
        await client.forward_messages(698038449, event.message)
    if '⚔️🥔' in event.raw_text:
        await client.forward_messages(698038449, event.message)
    if '⚔️🥔' in event.raw_text:
        await client.forward_messages(698038449, event.message)
    if '🛡🐉' in event.raw_text:
        await client.forward_messages(698038449, event.message)
    

@client.on(events.NewMessage(chats=(698038449), incoming = True ))
async def my_event_handler(event):
    if '/ping' in event.raw_text:
        await client.send_message(698038449, "ta on el bisho :)")

@client.on(events.NewMessage(chats=(960030071), incoming = True))
async def my_event_handler(event):
    if '/ping' in event.raw_text:
        await client.send_message(960030071, 'Timbrame en 5 min si no respondo, el movil 58698238')

@client.on(events.NewMessage(chats=(1166422074), incoming = True))
async def my_event_handler(event):
    if '/fight' in event.raw_text:
        await client.send_message(1166422074, 'Cogi ahi :D')

#loop.run_forever()

@client2.on(events.NewMessage(chats=('chtwrsbot'), incoming = True))
async def my_event_handler(event):
    global state
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        time.sleep(random.randint(30, 60))
        #await client.send_message('chtwrsbot', '/go')
        buttons = await event.get_buttons()
        for bline in buttons:
            for button in bline:
                if 'Intervene' in button.button.text:
                    await button.click()

#loop.run_forever()

@client3.on(events.NewMessage(chats=('chtwrsbot'), incoming = True))
async def my_event_handler(event):
    global state
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        time.sleep(random.randint(30, 60))
        #await client.send_message('chtwrsbot', '/go')
        buttons = await event.get_buttons()
        for bline in buttons:
            for button in bline:
                if 'Intervene' in button.button.text:
                    await button.click()
    
@client3.on(events.NewMessage(chats=(960030071)))
async def my_event_handler(event):
    if '/ping' in event.raw_text:
        await client.send_message(960030071, 'pong')

loop.run_forever()