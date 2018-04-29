#SideBot
import discord
import random
import requests
import time
import os
import asyncio
from discord.ext import commands
from discord.ext.commands import Bot
from Var import Hug 
from Var import Pat
from Var import Rem 
from Var import Nani
from Var import Couleurs


bot = commands.Bot(command_prefix='!')
emojis = bot.get_all_emojis()


@bot.event
async def on_ready():
	print ("SideBot pret")
	await bot.change_presence(game=discord.Game(name='!commandes'))

	
@bot.command(pass_context=True)
async def commandes(ctx):
	embed = discord.Embed(title="Commandes de SideBot", color=0x800000)
	embed.add_field(name="nani", value="NANI????", inline=False)
	embed.add_field(name="ping", value="dit pong", inline=False)
	embed.add_field(name="rem", value="Envoie une image de la meilleure waifu", inline=False)
	embed.add_field(name="avatar", value="Donne l'avatar d'un utilisateur", inline=False)
	embed.add_field(name="infos", value="Donne des informations sur un utilisateur", inline=False)
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def ping(ctx):
	await bot.say("pong")

@bot.command(pass_context=True)
async def neko(ctx):
	r = requests.get("https://cdn.nekos.life/neko/")
	await bot.say(r)
	

@bot.command(pass_context=True)
async def delete(ctx, nombre):
	admin = discord.utils.get(ctx.message.server.roles, id='416319027191873538')
	modo = discord.utils.get(ctx.message.server.roles, id='420960024437719050')
	if (ctx.message.author.top_role == admin) or (ctx.message.author.top_role == modo) :
		await bot.purge_from(ctx.message.channel, limit=int(nombre))
	else :
		await bot.say("Vous ne pouvez pas utiliser cette commande")



@bot.command(pass_context=True)
async def nani():
	embed = discord.Embed(color=0x6D1717)
	embed.set_image(url="https://imgur.com/{}".format(random.choice(Nani)))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def pat():
	embed = discord.Embed(color=0xFFC5DF)
	embed.set_image(url="https://cdn.nekos.life/pat/{}.gif".format(random.choice(Pat)))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def hug():
	embed = discord.Embed(color=0xFF1717)
	embed.set_image(url="https://i.imgur.com/{}.gif".format(random.choice(Hug)))
	await bot.say(embed=embed)

	
@bot.command(pass_context=True)
async def rem():
	embed = discord.Embed(color=0x33A8F1)
	embed.set_image(url="https://i.imgur.com/{}".format(random.choice(Rem)))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def nsfw(ctx):
	if ctx.message.channel.is_nsfw():
		await bot.say("oui")
	else:
		await bot.say("non")
		
@bot.command(pass_context=True)
async def say(ctx,message):
	emoji = discord.utils.get(emojis, id='420974322317000711')
	msg =str(message)
	await bot.say(msg)
	bot.add_reaction(msg,emoji)	

@bot.command(pass_context=True)
async def couleur(ctx, arg1, arg2=None):
	Arg1=str(arg1)
	if(Arg1.lower()=="reset"):
		roles = ctx.message.author.roles
		print(roles)
		print(len(roles))
		for i in range(0,len(roles)):
			nomRoles = roles[i].name
			print("nom role = ", nomRoles)
			if (nomRoles in Couleurs):
				nomRolesId = discord.utils.get(ctx.message.server.roles, name=nomRoles)
				await bot.remove_roles(ctx.message.author, nomRolesId)
				print(nomRoles,"enlevé")
			i += 1
			print(i)
			time.sleep(0.5)
		await bot.say("Votre couleur a bien été enlevée, si ce n'est pas le cas contacter un adminitrateur pour qu'il vous le fasse manuellement")
	elif(Arg1.lower()=="help"):
		CoulEmb = discord.Embed(title="La commande !couleur vous permet de changer la couleur de votre pseudo sur le serveur", color=0x0a00ff)
		CoulEmb.set_author(name="Guide de la commande !couleur")
		CoulEmb.add_field(name="Pour ajouter une couleur faites :", value="```!couleur + nomDeLaCouleur```", inline=False)
		CoulEmb.add_field(name="Pour enlever une couleur faites :", value="```!couleur - nomDeLaCouleur```", inline=False)
		CoulEmb.add_field(name="Pour réinisialliser vos couleurs faites :", value="```!couleur reset```", inline=False)
		CoulEmb.add_field(name="Voici les couleurs disponibles :", value=Couleurs, inline=False )
		await bot.say(embed=CoulEmb)
	elif(Arg1=="+"):
		Couleur=str(arg2)
		if(Couleur in Couleur):
			role = discord.utils.get(ctx.message.server.roles, name=Couleur.lower())
			await bot.add_roles(ctx.message.author, role)
		else:
			await bot.say("La couleur que vous voulez n'éxiste pas, pour voir les couleurs disponibles faites ```!couleur help```")
	elif(Arg1=="-"):
		Couleur=str(arg2)
		if(Couleur in Couleur):
			role = discord.utils.get(ctx.message.server.roles, name=Couleur.lower())
			await bot.remove_roles(ctx.message.author, role)
		else:
			await bot.say("La couleur que vous voulez n'éxiste pas, pour voir les couleurs disponibles faites ```!couleur help```")
	else:
		await bot.say("Vous vous etes trompé dans la commande, pour voir comment s'en servir faites : ```!couleur help```")
		


@bot.command(pass_context=True)
async def loveRem(ctx):
	role = discord.utils.get(ctx.message.server.roles, id='418870888906227712')
	await bot.add_roles(ctx.message.author, role)
	await bot.say("Bravo {} , vous avez maintenant le role Rem's Lover ! <:megThumbsup:420974322317000711>".format(ctx.message.author.name))

@bot.command(pass_context=True)
async def RemoveRole(ctx,role):
	role = discord.utils.get(ctx.message.server.roles, name=role)
	await bot.remove_roles(ctx.message.author, role)
	

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	embed = discord.Embed(title="Avatar de {}".format(user.name), color=0xff0000)
	embed.set_image(url=user.avatar_url)
	await bot.say(embed=embed)

	
@bot.command(pass_context=True)
async def infos(ctx, user: discord.Member):
    embed = discord.Embed(title="Info sur {}".format(user.name), color=0x00ff00)
    embed.add_field(name="Nom", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Statut", value=user.status, inline=True)
    embed.add_field(name="Plus haut role", value=user.top_role)
    embed.add_field(name="arrivé(e) le", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)


bot.run(os.environ.get('BOT_TOKEN'))
