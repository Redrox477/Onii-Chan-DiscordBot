import discord
from discord.ext import commands
import os
import requests
import embedlinks
import json
import phasmo
import datetime
import random
from rs import r_s
from oddoreven import o_e
from keep_alive import keep_alive

intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)

game_list = [
    '#relationship_status = find RELATIONSHIP STATUS {flames} between two people ',
    '\n more coming soon ..... uwu'
]

help_list = [
    '#hello - formal reply',
    '\n#goodmorning  - morning greetings',
    '\n#sed - inspirational qoutes',
    '\n#mock - duh, mock someone if i am in mood',
    '\n#roast - i am always ready to roast use #roast @"someone"',
    '\n#phasmo - Use only while playing phasmo ',
    '\n#games - fun and entertaining games list',
]

trouble_words = [
    'sad', 'depressed', 'angry', 'miserable', 'terrible', 'unhappy',
    'rough time', 'hurts'
]

encourage_phrases = [
    'Hang in there.', 'Don’t give up.', 'Keep pushing', 'Keep fighting!',
    'Stay strong.', 'Never give up.', 'Never gonna give up', 'Never say that.',
    'Come on! You can do it! / Onii-chan uwu.'
]


def get_qoute():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    qoute = json_data[0]['q'] + " - " + json_data[0]['a']
    return (qoute)


def get_roast():
    response = requests.get(
        "https://evilinsult.com/generate_insult.php?lang=en&type=json")
    json_data = json.loads(response.text)
    roast = json_data['insult']
    print(roast)
    return roast


#PHASMO_THREAD
@client.command()
async def phas(pic):
    bsc_evi = random.choice(phasmo.EVI)
    await pic.send(bsc_evi)
    await pic.send('Good luck ! lol')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="you Big Brother"))
    status = "{0.user} play begins... uwu".format(client)
    print(status)


@client.command()
async def waifu(msg):
    chosen_image = random.choice(embedlinks.waifuLinks)

    e = discord.Embed(colour=0xff69b4, timestamp=datetime.datetime.utcnow())
    e.set_image(url=chosen_image)
    e.set_footer(text=f"requested by : {msg.author.name}")
    await msg.send(embed=e)
    await msg.send("🥵")


@client.command()
async def ws(msg):
    chosen_series = random.choice(embedlinks.waifuSeries)
    await msg.send(chosen_series)
    await msg.send(f"requested by : {msg.author.name}")


@client.command()
async def kawaii(msg):
    await msg.send("💖")


@client.command()
async def wn(msg):
    chosen_name = random.choice(embedlinks.waifuName)
    await msg.send(chosen_name)
    await msg.send(f"requested by : {msg.author.name}")


@client.command()
async def hi(msg):
    #chosen_name = random.choice(embedlinks.waifuName)
    #await msg.send(chosen_name)
    await msg.send(f"hi {msg.author.name}")


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('#hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('#goodmorning'):
        await message.channel.send('Good Morning Onii sama !')

    if message.content.startswith('Ohayo!'):
        await message.channel.send('Ohayo Gozaimasu !')

    msg = message.content
    print(type(msg))
    print(msg)

    msg_list = msg.split()

    if message.content.startswith('#sed'):
        qoute = get_qoute()
        await message.channel.send(qoute)

    if message.content.startswith('#mock'):
        await message.channel.send('Not in the mood right now try #roast ')

    if msg.startswith('#roast'):
        roast_mentionlist = msg.split('#roast ', 1)[1]
        roast_mentionstr = str(roast_mentionlist)
        roast = get_roast()
        #print(roast_mentionstr)
        if roast_mentionstr in [
                '<@!908737295094530160>', "<@&909383892832755722>"
        ]:
            await message.channel.send('Vaipilla Raja')
            await message.channel.send(
                'https://tenor.com/view/seeman-gif-20044879')
        else:
            await message.channel.send(roast)
            await message.channel.send("didn't mean that.... " +
                                       roast_mentionstr + " uwu")

    for word in trouble_words:
        for msgs in msg_list:
            if msgs == word:
                await message.channel.send(random.choice(encourage_phrases))

    if msg == "<@!908737295094530160>" or msg == "<@&909383892832755722>" or msg == "@onichan":
        await message.channel.send('I am listening !')

    if msg == 'hmm' or msg == 'Hmm':
        await message.channel.send(f"hmm indeed {message.author.name} san")

    if message.content.startswith('#relationship_status'):
        await message.channel.send(
            'send boy name in the format , -b "boy name"')
        await message.channel.send(
            'send girl name in the format , -g "girl name"')
        await message.channel.send('then use #rs')

    global boy_name_str, girl_name_str

    if msg.startswith('-b'):
        boy_name = msg.split('-b', 1)[1]
        boy_name_str = str(boy_name)
    if msg.startswith('-g'):
        girl_name = msg.split('-g', 1)[1]
        girl_name_str = str(girl_name)

    if msg.startswith('#rs'):
        res = r_s(boy_name_str, girl_name_str)
        await message.channel.send(res)

    if msg.startswith('#phasmo'):
        await message.channel.send(
            '!basic - to get one random basic equipment (can be used again only if u had find the evidence using the before one)'
        )
        await message.channel.send(
            '!sec - to get a random secondary (non basic) equipments or items for stoinks '
        )
        await message.channel.send('Good luck lol !')

    if msg.startswith('#hru'):
        await message.channel.send('I am good thanks !')
    if msg == 'Rahul':
        await message.channel.send("is a bad boy")

    for msg in msg_list:
        if msg == 'sus' or msg == 'Sus':
            if message.author.id == 871710209695965244:
                await message.channel.send(
                    "I see you've copied mah style there")
            else:
                sus_links = embedlinks.sus
                sus_url = random.choice(sus_links)
                await message.channel.send(sus_url)

    if msg.startswith('#sendnukes'):
        rkrl_links = embedlinks.rkrl
        rkrl_url = random.choice(rkrl_links)

        await message.channel.send(rkrl_url)

    if msg.startswith('#help'):
        listtostr = ' '.join(map(str, help_list))
        await message.channel.send(listtostr)

    if msg.startswith('#games'):
        listtostr_game_list = ' '.join(map(str, game_list))
        await message.channel.send(listtostr_game_list)

    if msg_list[0] == 'are':
        if msg_list[1] == 'you':
            if msg_list[2] == 'okay':
                if msg_list[3] in [
                        '<@908737295094530160>', "<@&909383892832755722>"
                ]:
                    auth = 'Hai . Daijobu desu \nArigato ' + message.author.name + ' san'
                    print(auth)
                    await message.channel.send(auth)

    if msg.startswith('#odev'):
        odev = o_e()
        await message.channel.send(odev)

    await client.process_commands(message)


keep_alive()

try:

    client.run(os.getenv('TOKEN'))

except:

    os.system("kill 1")
