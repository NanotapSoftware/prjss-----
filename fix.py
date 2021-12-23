import discord
from discord.ext import commands
#other imports
import random
import os
import requests
import subprocess
import time
import sys
import platform
import math
import colorama
#end
#do not edit
get_token = input("Write a bot token:"+ "\n")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls();
#end

#hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
#r = requests.get("https://pastebin.com/raw/htqyimN4")


def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

#def Main_Program():
    #if hwid in r.text:
        #printSlow("Search for your system in the database..."+ "\n")
        #time.sleep(6)
        #printSlow("Successfully! Authorization is being performed...")
        #time.sleep(.1)
    #else:
       # printSlow("Search for your system in the database..."+ "\n")
       # time.sleep(6)
       # printSlow("Error! HWID Not I Database!"+ "\n")
        #printSlow("Please contact your system administrator. HWID: " + hwid + "\n")
        os.system('pause >NUL')

#if __name__ == "__main__":
    #Main_Program()



#main
token = f"{get_token}"
bot = commands.Bot(command_prefix='180!')
bot.remove_command('help')
#end
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls();

#on_ready = пишет в консоль когда бот заработал @bot.event
@bot.event
async def on_ready():
    print ("Статус - Online!")
    print ("Версия - 1.3")
    print ("Создатель - Тимур Сагдиев 7Д")
    print("Changelog -"+ "\n")
    print("-Added system protection"+ "\n")
    print("-Improved System authorization"+ "\n")


    activity = discord.Game(name="Netflix", type=1)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
#end
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls();


#-------------------------------------------------------------------------------------------------------------------------------


#help
@bot.command(aliases = ['help', 'HELP', 'Help', 'hELP', 'хелп', 'ХЕЛП', 'хЕЛП', 'Хелп', 'Хэлп', 'хЭЛП', 'ХЭЛП', 'хэлп'])
async def __help(ctx):
    embed=discord.Embed(title="Помощь по боту", description="👇Полный список команд 👇", color=0x20accf)
    embed.add_field(name="!help", value="Показывает данное окно", inline=False)
    embed.set_footer(text="Это ещё ранняя версия бота, он будет дорабатываться по мере необходимости")
    await ctx.send(embed=embed)
#end

#notif
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def notif(ctx, *, args, amount = 1):
    embed=discord.Embed(title="Внимание!", description="👇 Сообщение от учителя 👇", color=0x20accf)
    embed.add_field(name=f'{args}', value=f'@everyone', inline=False)  
    await ctx.channel.purge(limit = amount);
    await ctx.send(embed=embed)
#end


#ad_help
@bot.command()
@commands.has_permissions(administrator = True)
async def ad_help(ctx, amount = 1):
    embed=discord.Embed(title="Помощь по боту", description="👇Полный список команд для администратора 👇", color=0x20accf)
    embed.add_field(name="!help", value="Показывает данное окно", inline=False)
    embed.add_field(name="!ad_help", value="Показывает данное окно", inline=False)
    embed.add_field(name="!notif", value="Создать уведомление для учеников", inline=False)
    embed.add_field(name="!clear", value="Отчистить чат", inline=False)
    embed.set_footer(text="Это ещё ранняя версия бота, он будет дорабатываться по мере необходимости")
    await ctx.channel.purge(limit = amount);
    await ctx.send(embed=embed)
#end

#clear
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    embed=discord.Embed(title="Чат отчищен", description="👇 Подробности ниже 👇", color=0x20accf)
    embed.add_field(name="Чат успешно был отчистен!", value=f"Было удалено {amount} строк", inline=False)
    await ctx.send(embed=embed)
#end


#ban
@bot.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    embed=discord.Embed(title="Успешно!", description= f"👇Пользователь - {discord.Member} был заблокирован! 👇", color=0x20accf)
    embed.add_field(name=f"Причина - {reason}", value=f"", inline=False)
    await member.ban(reason = reason)
    await ctx.send(embed=embed)
#end

#tz - 
#




#run
bot.run(token)
#end 