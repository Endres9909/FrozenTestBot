import os
import json
import discord
import datetime 
from os import getenv
from discord import app_commands

with open("errors.json","r") as e:
  errors = json.load(e)

  
class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=discord.Object(id=getenv('MY_GUILD')))
        await self.tree.sync(guild=discord.Object(id=getenv('MY_GUILD')))
      
intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
  print('---------------------------------------')
  print('{0.user} is working!'.format(client))
  print('---------------------------------------')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Frozen Freebies'))
  
  
  
@client.tree.command(name = 'error_name', description = 'Search the error by its name to get a possible solution')
async def error_name(interaction: discord.Interaction, error: str):
  for list in errors['list_errors']:
    if str(list['name']).startswith(error):
      
      name = list['name']
      id = list['id']
      common = list['common']
      type = list['type']
      solution = list['solution']
      note = list['note']
      color = list['color']
      
      if list['color'] == 'discord.Color.purple()':
        color = discord.Color.purple()
      elif list['color'] == "discord.Color.orange()":
        color = discord.Color.orange()
      elif list['color'] == "discord.Color.red()":
        color = discord.Color.red()
      emb = discord.Embed(title='Error', description=name, color=color)
      emb.set_footer(text='Frozen Freebies Errors')
      emb.timestamp = datetime.datetime.now()
      emb.set_author(
          name='Frozen Freebies',
          icon_url= 'https://pbs.twimg.com/profile_images/1542644644982423553/huthtNbr_400x400.png')
      emb.add_field(name='Common', value=common, inline=True)
      emb.add_field(name='Type of Error', value=type, inline=True)
      emb.add_field(name='Error ID', value=id, inline=True)
      emb.add_field(name='What it means and possible solution',
                    value=solution,
                    inline=False)
      emb.add_field(name='NOTE', value=note, inline=False)
      await interaction.response.send_message(embed=emb)
      
    # <--------------------------------------------------------------------------------------------->

@client.tree.command(name = 'error_id', description = 'Search the error by its ID to get a possible solution')
async def error_id(interaction: discord.Interaction, id: int):
  for list in errors['list_errors']:
    if list['id'] == id:
      
      name = list['name']
      id = list['id']
      common = list['common']
      type = list['type']
      solution = list['solution']
      note = list['note']
      color = list['color']
      
      if list['color'] == 'discord.Color.purple()':
        color = discord.Color.purple()
      elif list['color'] == "discord.Color.orange()":
        color = discord.Color.orange()
      elif list['color'] == "discord.Color.red()":
        color = discord.Color.red()

      emb = discord.Embed(title='Error', description=name, color=color)
      emb.set_footer(text='Frozen Freebies Errors')
      emb.timestamp = datetime.datetime.now()
      emb.set_author(
          name='Frozen Freebies',
          icon_url= 'https://pbs.twimg.com/profile_images/1542644644982423553/huthtNbr_400x400.png')
      emb.add_field(name='Common', value=common, inline=True)
      emb.add_field(name='Type of Error', value=type, inline=True)
      emb.add_field(name='Error ID', value=id, inline=True)
      emb.add_field(name='What it means and possible solution',
                    value=solution,
                    inline=False)
      emb.add_field(name='NOTE', value=note, inline=False)
      await interaction.response.send_message(embed=emb)

    # <--------------------------------------------------------------------------------------------->

@client.tree.command(name = 'info', description = 'Displays information about specific users')
async def info(interaction: discord.Interaction, user: discord.Member):
  emb = discord.Embed(title="{}'s Info".format(user.name), description="Here's What I could Find About " + format(user.name), color=discord.Color.purple())
  emb.set_author(name='Frozen Freebies',icon_url='https://pbs.twimg.com/profile_images/1542644644982423553/huthtNbr_400x400.png')
  emb.timestamp = datetime.datetime.now()
  emb.add_field(name="Name", value=user.name, inline=True)
  emb.add_field(name="ID", value=user.id, inline=True)
  emb.add_field(name="Status", value=user.status, inline=False)
  emb.add_field(name="Top Role", value=user.top_role, inline=True)
  emb.add_field(name="Joined At", value=user.joined_at.strftime("%b %d, %Y, %T"), inline=True)
  emb.set_thumbnail(url=user.avatar.url)
  emb.set_footer(text='Frozen Freebies Info')
  await interaction.response.send_message(embed=emb)

    # <--------------------------------------------------------------------------------------------->
  
@client.tree.command(name = 'guide', description = 'Frozen Freebies Documentation')
async def guide(interaction: discord.Interaction):
  emb = discord.Embed(title='Frozen Freebies Documentation',description="Please be sure to read this information upon entering the server, and refer back to it before opening a <#986830467024162827>",color=discord.Color.purple())
  emb.set_author(name='Frozen Freebies',icon_url='https://pbs.twimg.com/profile_images/1542644644982423553/huthtNbr_400x400.png')
  emb.timestamp = datetime.datetime.now()
  emb.add_field(name='Documentation covering the usage of Frozen Freebies software',value='[General Guide](https://frozen-freebies.gitbook.io/frozen-freebies-2.0-guide/)',inline=False)
  emb.add_field(name='Video covering overview and setup of Frozen Freebies software',value='[Video Setup Guide](https://www.youtube.com/watch?v=ueVDZH8R84w)',inline=False)
  emb.add_field(name='Documentation and reference list of known errors',value='[List of Common Errors](https://docs.google.com/spreadsheets/u/1/d/1H_SrQPHo5y-qGS9qfctwdmvlLHqk-DnytVA0g92oqbs/edit?usp=sharing)',inline=False)
  emb.add_field(name='Frozen Dashboard',value='[Dashboard](https://dashboard.frozensoftware.com)',inline=False)
  emb.add_field(name='Announcements', value='<#939644999644106842>', inline=True)
  emb.add_field(name='Bot Download', value='<#939648451145236483>', inline=True)
  emb.add_field(name='FAQ', value='<#941424987590516827>', inline=True)
  emb.add_field(name='\u200b',value='\u200b',inline=True)
  emb.add_field(name='Official Twitter Account',value='[Twitter](https://twitter.com/FreebiesFrozen)',inline=False)
  emb.set_footer(text='Frozen Freebies Guide')
  await interaction.response.send_message(embed=emb)

    # <--------------------------------------------------------------------------------------------->
  
@client.tree.command(name = 'help', description = 'Frozen Freebies commands and how to use them')
async def help(interaction: discord.Interaction):  
  emb = discord.Embed(title='Frozen Freebies Help',description="Here is a list of the most useful Frozen Freebies commands and how to use them‍",color=discord.Color.purple())
  emb.set_author(name='Frozen Freebies',icon_url='https://pbs.twimg.com/profile_images/1542644644982423553/huthtNbr_400x400.png')
  emb.timestamp = datetime.datetime.now()
  emb.add_field(name='/error_id',value='Search the error by its ID that is display on you webhook, and get a possible solution or what the error means',inline=False)
  emb.add_field(name='/error_name',value='Search the error by its name that is display on you webhook, and get a possible solution or what the error means',inline=False)
  emb.add_field(name='/info',value='Display all user information, including discord name, discord id, status, top role, and when they joined the server',inline=False)
  emb.add_field(name='/guide',value='Display Frozen Freebies Documentation',inline=False)
  emb.add_field(name='FAQ', value='<#941424987590516827>', inline=False)
  emb.add_field(name='\u200b',value='\u200b',inline=True)
  emb.add_field(name='Official Twitter Account',value='[Twitter](https://twitter.com/FreebiesFrozen)',inline=False)
  emb.set_footer(text='Frozen Freebies Help')
  await interaction.response.send_message(embed=emb)

    # <--------------------------------------------------------------------------------------------->
  
@client.tree.command(name = 'partners', description = 'Frozen Freebies Partners')
async def partners(interaction: discord.Interaction):
               
  emb = discord.Embed(title='Frozen Freebies Partners',color=discord.Color.purple())
  emb.set_author(name='Frozen Freebies',icon_url='https://pbs.twimg.com/profile_images/1542644644982423553/huthtNbr_400x400.png')
  emb.timestamp = datetime.datetime.now()
  emb.add_field(name='__Servers__',value='\u200b',inline=False)
  emb.add_field(name='Arson Server',value='<#941018747957825596>',inline=True)
  emb.add_field(name='Sauce Server',value='<#952990614876745728>',inline=True)
  emb.add_field(name='Zesty Server',value='<#996231374744858664>',inline=True)
  emb.add_field(name='__Proxies__',value='\u200b',inline=False)
  emb.add_field(name='Bezos Proxies',value='<#969225210249220216>',inline=True)
  emb.add_field(name='Chimp Proxies',value='<#994372754591711292>',inline=True)
  emb.add_field(name='Polar Proxies',value='<#1002052718275330128>',inline=True)
  emb.add_field(name='Profit Proxies',value='<#987093364266643466>',inline=True)
  emb.add_field(name='Stella Proxies',value='<#954204233459200010>',inline=True)
  emb.add_field(name='Unknown Proxies',value='<#1002701641700606043>',inline=True)
  emb.add_field(name='\u200b',value='\u200b',inline=True)
  emb.add_field(name='Official Twitter Account',value='[Twitter](https://twitter.com/FreebiesFrozen)',inline=False)
  emb.set_footer(text='Frozen Freebies Partners')
  await interaction.response.send_message(embed=emb)
  
    # <--------------------------------------------------------------------------------------------->
  
@client.tree.command(name = 'version', description = 'Display the latest software version and its respect OS version')
async def version(interaction: discord.Interaction):
  with open("version.json","r") as v:
    version = json.load(v)

    windows_os = version["version"][0]["os"]
    windows_version = version["version"][0]["version"]
    windows_link = version["version"][0]["link"]
    macos_os = version["version"][1]["os"]
    macos_version = version["version"][1]["version"]
    macos_link = version["version"][1]["link"]

    emb = discord.Embed(title='Frozen Freebies Version',color=discord.Color.purple())
    emb.set_author(name='Frozen Freebies',icon_url='https://pbs.twimg.com/profile_images/1542644644982423553/huthtNbr_400x400.png')
    emb.timestamp = datetime.datetime.now()
    emb.add_field(name='__Windows__',value='\u200b',inline=False)
    emb.add_field(name='OS',value=windows_os,inline=True)
    emb.add_field(name='Version',value=windows_version,inline=True)
    emb.add_field(name='Link',value=windows_link,inline=True)
    emb.add_field(name='__macOS__',value='\u200b',inline=False)
    emb.add_field(name='OS',value=macos_os,inline=True)
    emb.add_field(name='Version',value=macos_version,inline=True)
    emb.add_field(name='Link',value=macos_link,inline=True)
    emb.add_field(name='Official Twitter Account',value='[Twitter](https://twitter.com/FreebiesFrozen)',inline=False)
    emb.set_footer(text='Frozen Freebies Version')
    await interaction.response.send_message(embed=emb)
  
client.run(getenv('TOKEN'))
