# Botten laget av PowerKuz ©

import pytz
import datetime
import os
import random
import sys

import discord
from discord.ext import commands
from discord.ext.commands import Bot

d = os.path.dirname(os.path.abspath(__file__))

norway = pytz.timezone('Europe/Oslo')
date = datetime.datetime.now(norway)

monde = 11

timeMin = 21
timeMax = 21

token = 'NzgwNDczMjMyMjAwNjk1ODI5.X7vmVw.MXkn0Q35gSqRTxrX_KEcDXY-5Ps'

if datetime.datetime.now(norway).month != monde:
    print('Ikke jul endå')
    sys.exit()

print("Starter discord bot på version  > " + str(discord.version_info))
print("Botten laget av PowerKuz ©")

def Wait(day, h, tid):
    if date.day == day and date.hour == tid:
        f = f'{str(day)}.txt'

        msg = []
        svar = ''
        win = ''
        url = ''
        for l in open(d + '\\' + f, 'r').readlines(): 
            if l != '\n':
                msg.append(l.strip())
        
        for l in msg:
            if l.lower().startswith('_svar_'):
                o = l.split('=')[1].strip().lower()
                msg.remove(l)
                svar = o

        for l in msg:
            if l.lower().startswith('_win_'):
                o = l.split('=')[1].strip().lower()
                msg.remove(l)
                win = o
        
        for l in msg:
            if l.lower().startswith('_hide_'):
                msg.remove(l)
        
        for l in msg:
            if l.lower().startswith('_url_'):
                o = l.split('=')[1].strip().lower()
                msg.remove(l)
                url = o

        return (msg, svar, win, url)
    return None

def color(msg):
    yaml = f"""
**{msg}**
"""
    return yaml

bot = Bot('')
@bot.event
async def on_ready():
    for s in bot.guilds:
        await s.text_channels[0].send(color("Er det noen snille barn her, HAHAHAHAH, HOHOHO. Send meg en DM\n Kommandoer > info"))

    date = datetime.datetime.now(norway)

    i = input('Botten er startet skal jeg vente på dagens kalender ja/nei > ')
    if i.lower() == 'ja':
        tid = random.randint(timeMin, timeMax)
        print('Venter på dagens Dag > ' + str(date.day) + ' Time > ' + str(tid))
        while True:
            date = datetime.datetime.now(norway)
            w = Wait(date.day, date.hour, tid)
            if w:
                print('Starter > ' + str(date))
                break

    

    if w:
        fullmsg = ''
        svar = w[1]
        win = w[2]
        url = w[3]

        for idx, l in enumerate(w[0]):
            if not idx+ 1 == len(w[0]):
                fullmsg += l + '\n'
            else:
                fullmsg += l

        for s in bot.guilds:
            discord_msg = await s.text_channels[0].send(color('@everyone\n' + fullmsg))

            await discord_msg.add_reaction('🅰️')
            await discord_msg.add_reaction('🅱️')
            await discord_msg.add_reaction('\U0001f1e8')


            if svar == 'a':
                ja = '🅰️'
            if svar == 'b':
                ja = '🅱️'
            if svar == 'c':
                ja = '\U0001f1e8'
            
            done_users = []
            def check(reaction, user):
                if not user in done_users:
                    done_users.append(user)
                    return str(reaction.emoji) == ja and user != bot.user
            try:
                reaction, user = await bot.wait_for('reaction_add', timeout=300, check=check)
                if url:
                    await s.text_channels[0].send(color(f'HOHOHO der var du rask!, Gratulerer {user.name} {win}')  + f'{url}')
                else:
                    await s.text_channels[0].send(color(f'HOHOHO der var du rask!, Gratulerer {user.name} {win}'))
            except:
                await s.text_channels[0].send(color('HOHO, du fikk ingen pakke siden du var drit treig, hilsen nissen.'))



        tid = random.randint(timeMin, timeMax)
        print('Venter på neste Dag > ' + str(date.day + 1) + ' Time > ' + str(tid))
        while True:
            date = datetime.datetime.now(norway)
            w = Wait(date.day + 1, date.hour, tid)
            if w:
                print('Starter > ' + str(date))
                break


@bot.command()
async def info(ctx):
    await ctx.send("**En julekalender bot som er laget av PowerKuz©, i sammerbeid med mutlu(Ikke Henrik eller famdritt), HOHOHOHO.**")


bot.run(token)
        
