import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='ga!', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.event
async def on_member_join(member):
    await member.send(
        'Olá! Bem-vindo(a) ao servidor! \n\n'
        'Meu prefixo é: ga!\n'
        'Aqui uma lista de comandos:\n'
        'ga!pet - Ideias reciclando garrafas pet!\n'
        'ga!lacre - Ideias reciclando lacres de latinhas ou tampinhas de garrafas!\n'
        'ga!lat - Ideias reciclando latinhas de refrigerante!\n'
        'ga!ret - Ideias utilizando retalhos e roupas velhas!\n'
    )

@bot.command()
async def ajuda(ctx):
    await ctx.send(
        'Olá! Eu sou o Gaiart, bot de ideias de artesanatos reciclaveis!\n\n' 
        'Meu prefixo é: ga!\n\n'
        'Aqui uma lista de comandos:\n'
        'ga!pet - Ideias reciclando garrafas pet!\n'
        'ga!lacre - Ideias reciclando lacres de latinhas ou tampinhas de garrafas!\n'
        'ga!lat - Ideias reciclando latinhas de refrigerante!\n'
        'ga!ret - Ideias utilizando retalhos e roupas velhas!\n'
    )

@bot.command()
async def pet(ctx):
    img_name = random.choice(os.listdir('Garrafas.pet'))
    # E é assim que você pode substituir o nome do arquivo por uma variável!
    with open(f'Garrafas.pet/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def lat(ctx):
    img_name = random.choice(os.listdir('Latinhas'))
    # E é assim que você pode substituir o nome do arquivo por uma variável!
    with open(f'Latinhas/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def ret(ctx):
    img_name = random.choice(os.listdir('Retalhos'))
    # E é assim que você pode substituir o nome do arquivo por uma variável!
    with open(f'Retalhos/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def lacre(ctx):
    img_name = random.choice(os.listdir('Lacres.tampinhas'))
    # E é assim que você pode substituir o nome do arquivo por uma variável!
    with open(f'Lacres.tampinhas/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

bot.run("-")
