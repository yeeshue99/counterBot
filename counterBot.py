# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import discord
from discord.ext import commands
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='+')


rations=0
values=[]
counters=[]

print(discord.__version__)

@bot.command()
async def test(arg):
    await bot.say(arg)
    await bot.say('%s'%(type(arg)))

@bot.command()
async def counterList():
    global counters
    await bot.say("The current list of counters is: %s"%(values[currentCounter],counters[currentCounter]))

@bot.command()
async def newCounter(ctx):
    global counters
    global values
    counters.append(str(ctx))
    values.append(0)
    await bot.say("The current list of counters is: %s" %(counters))

@bot.command()
async def setCounter(ctx, arg):
    global counters
    global values
    assert ctx in counters
    currentCounter = counters.index(ctx)
    values[currentCounter] = int(arg)
    await bot.say("There are now %s in the %s counter."%(values[currentCounter],counters[currentCounter]))

@bot.command()
async def currentCounters(ctx):
    global counters
    global values
    assert ctx in counters
    currentCounter = counters.index(ctx)
    await bot.say("There are now %s in the %s counter."%(values[currentCounter],counters[currentCounter]))
    
@bot.command()
async def counterDown(ctx):
    global counters
    global values
    assert ctx in counters
    currentCounter = counters.index(ctx)
    if values[currentCounter] <= 0:
        await bot.say("The counter is currently empty. The action couldn't be performed")
    else:
        values[currentCounter] -= 1
        await bot.say("There are now %s in the %s counter."%(values[currentCounter],counters[currentCounter]))

@bot.command()
async def counterDownMass(ctx, arg):
    global counters
    global values
    assert ctx in counters
    currentCounter = counters.index(ctx)  
    values[currentCounter] -= int(arg)
    if values[currentCounter] <= 0:
        await bot.say("The counter doesn't have enough to complete this action.")
        values[currentCounter] += arg
    else:
        await bot.say("There are now %s in the %s counter."%(values[currentCounter],counters[currentCounter]))
        
bot.run("NDA3NzU5MjkxNzgxNzQyNTkz.DVGlFQ.Lyo2t9wPoZLp1DrPxbhSfSsaGuY")