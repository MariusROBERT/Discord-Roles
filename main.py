import discord
from discord.ext import tasks, commands
import json

fileJson = "token.json"
with open(fileJson, "r") as f:
    infos = json.load(f)
token = infos["tokenDiscord"]
id_server = infos["idServeur"]
liste_roles = infos["roles"]
blabla = """Bienvenue sur le serveur discord du DUT Informatique
Afin d'obtenir vos rôles, merci de m'indiquer dans quelle classe vous êtes"""



client = discord.Client()

@client.event
async def on_member_join(member):
    await client.send_message(member, blabla)

@client.event
async def on_message(message):
    if message.author.bot == True:
        return

    if type(message.channel) == discord.channel.DMChannel:
        texte = message.content
        user = message.channel.recipient
        print("{} from {}".format(texte, user))

        for i in liste_roles:
            if i in texte:
                #add_role(message.author)
                serveur = client.get_guild(id_server)
                #print(serveur.name)
                #print(user.mention[2:-1])
                #print(user.roles)
                #print(serveur.members)
                member = serveur.get_member(int(user.mention[2:-1]))
                print(member.joined_at)
                #await edit(roles= )
                role = discord.utils.get(serveur.roles, name=i)
                await member.add_roles(role, reason="Seig Role Bot")
                await message.author.send("Un rôle vous a été assigné")
                return



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #await client.change_presence(activity=discord.Game(name='Send message to get a role'))

client.run(token)
