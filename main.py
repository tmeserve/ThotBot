import discord
import os

client = discord.Client()
@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)

@client.event
async def on_message(message):
    if message.content.lower().startswith("!thots")\
            or message.content.lower().startswith("!thot"):
        split = message.content.split()
        await client.send_message(message.channel, "Grabbing thot pics babes.")
        if len(split) == 3:
            split_int = int(split[2])
            if split_int > 20:
                split_int = 20
            await splitOps(split, message.channel, amount=str(split_int))
        elif len(split) == 2:
            split = message.content.split()
            await splitOps(split, message.channel)
    elif message.content.lower().startswith("!m") \
        or message.content.lower().startswith("!mute"):
        split = message.content.split()

        await client.send_message(message.channel, "Muting this {0}'s bitch ass".format(split[0]))



async def splitOps(split, channel, amount="1"):
    if split[1][0] == "#":
        stripped = split[1].strip("#")
        osSystem("--tag " + stripped, amount)
        await send_messages(channel, os.getcwd() + "\\" + stripped)
    else:
        osSystem(split[1], amount)
        await send_messages(channel, os.getcwd() + "\\" + split[1])


def osSystem(arg1, amount):

    os.system("instagram-scraper " + arg1 + " --maximum " + amount +
              " -u Fazedude123 -p M1n3craftkillz123 -q")

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)

async def send_messages(channel, dir, delete=True):
    count = 0
    for filename in os.listdir(dir):
        path = dir + "\\" + filename
        size = file_size(path)
        ssize = size.split()
        size2 = float(ssize[0])
        if ssize[1] == "MB" and size2 >= 8.0:
            await client.send_message(channel, "Skipping file " + filename + " as it's too large")
            continue
        await client.send_file(channel, path, filename=filename)
        print("One file await")
        count += 1

    if delete:
        os.system("rmdir /Q /S " + dir)
    await client.send_message(channel, "enjoy bitches")

client.run('')
