import discord
import os
from random import randint
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(':Привет'):
        await message.channel.send('qq')
        await message.channel.send('Меня зовут S1lif BOT, я создан для развлечения и общения! Я надеюсь я смогу помочь твоему серверу!')
        await message.channel.send('Прописав команду :Help я тебе покажу мои функции!')
        await message.channel.send('Что бы попрощаться напиши :Пока')



    if message.content.startswith(':Монетка'):
      win_number = 1
      current_number = randint(1, 2)
      if current_number == win_number:
        await message.channel.send('Опа! Ты выйграл, поздравляю!')
      else:
        await message.channel.send('Ты проиграл, сорян!')

    

    if message.content.startswith(':Help'):
      await message.channel.send('Мои категории:')
      await message.channel.send(':Игры')
      await message.channel.send(':что-бы все проснулись')




    if message.content.startswith(':что-бы все проснулись'):
      await message.channel.send('@everyone')



    if message.content.startswith(':Игры'):
      await message.channel.send(':Монетка - Игра основанная на игре Орёл-Решка!')
      await message.channel.send(':Imp - вы задаёте боту вопрос не предатель ли ты')



    if message.content.startswith(':Imp'):
      win_number = 1
      current_number = randint(1, 2)
      if current_number == win_number:
        await message.channel.send('Да!')
      else:
        await message.channel.send('Нет!')




    if message.content.startswith(':Пока'):
      await message.channel.send('Пока!')
    


client.run(os.environ['TOKEN'])