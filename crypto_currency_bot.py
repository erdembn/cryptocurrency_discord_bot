import discord
import requests
import json

#add your token here
TOKEN = ""


client = discord.Client()


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f"{username}: {user_message} ({channel})")
  if message.author == client.user:
    return
    #this bot works only for this specific channel, you can change this line
  if message.channel.name == "price": 
    try:
        user_message=user_message.lower()
        #getting random facts from api  
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={user_message}&vs_currencies=usd")
        price = response.json()
        if price:
          await message.channel.send(f"${price[user_message]['usd']}")
          return
        else:
          raise ValueError
        
    except ValueError:
        await message.channel.send("Sorry, can you try again\nYou need to type cryptocurrency's name")
        return

    


client.run(TOKEN)