import discord
from discord.ext import tasks, commands
import json

fileJson = "token.json"
with open(fileJson, "r") as f:
    infos = json.load(f)
token = infos["tokenDiscord"]
id_server = infos["idServeur"]
liste_roles = infos["roles"]
banlist = infos["banlist"]
blabla = """Bienvenue sur le serveur discord du DUT Informatique
Afin d'obtenir vos rôles, merci de m'indiquer dans quelle classe vous êtes (ex : A1)"""

intents = discord.Intents.default()
intents.members = True


client = discord.Client(intents=intents)


def addBanList(id):
    with open(fileJson, "w") as f:
        infos["banlist"].append(id)
        infos = json.dump(infos, f)



@client.event
async def on_member_join(member):
    print(member)
    await member.send(blabla)
    #await client.send_message(member, blabla)

@client.event
async def on_message(message):
    if message.author.bot == True or message.author.id in banlist:
        return

    if type(message.channel) == discord.channel.DMChannel:
        texte = message.content
        user = message.channel.recipient
        print("{} from {}".format(texte, user))

        for i in liste_roles:
            if i in texte.lower():
                #add_role(message.author)
                print(id_server)
                print(type(id_server))
                serveur = client.get_guild(id_server)
                print(serveur.name)
                #print(user.mention[2:-1])
                #print(user.roles)
                #print(serveur.members)
                #member = serveur.get_member(int(user.mention[2:-1]))
                #print(message.author.joined_at)
                #await edit(roles= )
                role = discord.utils.get(serveur.roles, name=i)
                await message.author.add_roles(role, reason="Bot de Marius")
                await message.author.send("Un rôle vous a été assigné")
                addBanList(message.author.id)
                return
        await message.author.send("Désolé, cette classe n'est pas reconnue, veuillez re-essayer")




@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #await client.change_presence(activity=discord.Game(name='Send message to get a role'))

client.run(token)
