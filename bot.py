import discord
import asyncio
import os
from datetime import *
from discord.ext import commands, tasks
from time import *

client = discord.Client()
m = str("https://us02web.zoom.us/j/3938580099?pwd=bzV5MWN4aUwvd2lITzZJcGdUUEd4UT09 회의 ID: 393 858 0099 암호: 1234")
file = ['','','','','','']
file[0]=discord.File("C:/Users/H/Pictures/Saved Pictures/mm_y.png") #무민 응
file[1]=discord.File("C:/Users/H/Pictures/Saved Pictures/mm_n.png") #무민 아니
file[2]=discord.File("C:/Users/H/Pictures/Saved Pictures/icon_27.gif") #라이젠 움짤


@client.event
async def on_ready(): # 봇이 실행 준비가 되었을 때 행동할 것
    print('Logged in as')
    print(client.user.name) # 클라이언트의 유저 이름을 출력합니다.
    print(client.user.id) # 클라이언트의 유저 고유 ID를 출력합니다.
    # 고유 ID는 모든 유저 및 봇이 가지고있는 숫자만으로 이루어진 ID입니다.
    print('------')


@client.event
async def on_message(message): # 입력되는 메세지에서 찾기
    if message.content == '!sex': # 만약 메세지가 ''으로 시작된다면
        await message.channel.send('기분 딱좋노') # 클라이언트는 메세지가 올라온 채널에 ''을 보냅니다.

    if message.content == '!pong':
        await message.channel.send('ping!')

    if message.content == '!zoom':
        await message.channel.send('줌 출석해라' +' '+ m)
    
    if message.content == '!자가진단':
        await message.channel.send('자가진단해라'+ ' '+ ' https://hcs.eduro.go.kr/')

    if message.content == '최지':
        await message.channel.send('우수')

    if message.content == '예아':
        await message.channel.send('안될거뭐있노')

    if message.content == '노무현':
        await message.channel.send('살아있음')

    if message.content == '서준아':
        await message.channel.send('------------------------------------------최지우수 방지선------------------------------------')

    if message.content == '잘자':
        await message.channel.send('good night')

    if message.content == '니노':
        await message.channel.send('여쉰님')

    if message.content == '무현':
        await message.channel.send('운지')

    if message.content == 'ㅈㅈ':
        await message.channel.send('쥬지')

    if message.content == 'ㅂㅈ':
        await message.channel.send('뷰지')

    if message.content == '이승민':
        await message.channel.send('')

    if message.content == '가온':
        await message.channel.send('첼시')

    if message.content == '동균':
        await message.channel.send('방예나')

    if message.content == '무민':
        await message.channel.send('https://ifh.cc/v-563Hah')

    if message.content == '무민 응':
        await message.channel.send(file=file[0])

    if message.content == '무민 아니':
        await message.channel.send(file=file[1])

    if message.content == '라이젠':
        await message.channel.send(file=file[2])

    if message.content == '자러감':
        await message.channel.send('https://media.tenor.co/videos/f8eced6672e047296d570055f129b13d/mp4')
    








access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

