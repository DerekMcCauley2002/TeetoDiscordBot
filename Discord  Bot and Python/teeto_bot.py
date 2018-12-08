import discord
import random
import requests
import json


from collections import Counter
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ('?')
TOKEN = **
RIOTAPI = 'RGAPI-1382429f-f16b-4610-b17e-70510bc9a0a4'

client = Bot(command_prefix=BOT_PREFIX)

num2words = {1: 'Annie', 2: 'Olaf', 3: 'Galio', 4: 'Twisted Fate', 5: 'Xin Zhao', \
			6: 'Urgot', 7: 'LeBlanc', 8: 'Vladimir', 9: 'Fiddlesticks', 10: 'Kayle', \
			11: 'Master Yi', 12: 'Allistar', 13: 'Ryze', 14: 'Sion', \
			15: 'Sivir', 16: 'Soraka', 17: 'Teemo', 18: 'Tristana', \
			19: 'Warwick', 20: 'Nunu & Willump', 21: 'Miss Fortune', 22: 'Ashe', \
			23: 'Tryndamere', 24: 'Jax', 25: 'Morgana', 26: 'Zilean', \
			27: 'Singed', 28: 'Evelynn', 29: 'Twitch', 30: 'Karthus', \
			31: "Cho'Gath", 32: 'Amumu', 33: 'Rammus', 34: 'Anivia', \
			35: 'Shaco', 36: 'Dr. Mundo', 37: 'Sona', 38: 'Kassadin', \
			39: 'Irelia', 40: 'Janna', 41: 'Gangplank', 42: 'Corki', \
			43: 'Karma', 44: 'Taric', 45: 'Veigar', \
			48: 'Trundle', 50: 'Swain', \
			51: 'Caitlyn', 53: 'Blitzcrank', 54: 'Malphite', \
			55: 'Katarina', 56: 'Nocturne', 57: 'Maokai', 58: 'Renekton', \
			59: 'Jarvan IV', 61: 'Orianna', 62: 'Wukong', \
			63: 'Brand', 64: 'Lee Sin', \
			67: 'Vayne', 68: 'Rumble', 69: 'Cassiopeia', \
			72: 'Skarner', 74: 'Heimerdinger', \
			75: 'Nasus', 76: 'Nidalee', 77: 'Udyr', 78: 'Poppy', \
			79: 'Gragas', 80: 'Pantheon', 81: 'Ezreal', 82: 'Mordekaiser', \
			83: 'Yorick', 84: 'Akali', 85: 'Kennen', 86: 'Garen', \
			89: 'Leona', 90: 'Malzahar', \
			91: 'Talon', 92: 'Riven', \
			96: "Kog'Maw", 98: 'Shen', \
			99: 'Lux', 101: 'Xerath', 102: 'Shyvana', \
			103: 'Ahri', 104: 'Graves', 105: 'Fizz', 106: 'Volibear', \
			107: 'Rengar', 110: 'Varus', \
			111: 'Nautilus', 112: 'Viktor', 113: 'Sejuani', 114: 'Fiora', \
			115: 'Ziggs', 117: 'Lulu', \
			119: 'Draven', 120: 'Hecarim', 122: 'Darius', \
			126: 'Jayce', \
			131: 'Diana', 518: 'Neeko', \
			143: 'Zyra', 145: "Kai'Sa", \
			516: 'Ornn', 498: 'Xayah', 497: "Rakan", 150: 'Gnar', \
			432: 'Bard', 429: 'Kalista', 427: "Ivern", 154: 'Zac', \
			421: "Rek'Sai", 420: 'Illaoi', 157: "Yasuo", 412: 'Thresh', \
			268: 'Azir', 267: 'Nami', 161: "Velkoz", 266: 'Aatrox', \
			163: 'Taliyah', 164: 'Camille', 201: "Braum", 202: 'Jhin', \
			203: 'Kindred', 222: 'Jinx', 223: "Tahm Kench", 236: 'Lucian', \
			238: 'Zed', 240: 'Kled', 245: "Ekko", 254: 'Vi'}

@client.command(name='8ball')
async def eight_ball():
	possible_responses = [
		'That is a resounding no',
		'It is not looking likely',
		'Too hard to tell',
		'It is quite possible',
		'Definitely',
	]
	await client.say(random.choice(possible_responses))

@client.event
async def on_ready(): #startup code
	await client.change_presence(game=Game(name="to the lord's strengths"))
	print('Logged in as ' + client.user.name)

@client.event #help command
async def on_message(message):
	if message.content.startswith('?help'):
		embed = discord.Embed(title='Teeto Bot Help', description='Description of all current commands.', color=0xc45100)
		embed.add_field(name='?8ball', value='Sends a random lucky message for your pleasure.', inline=False)
		embed.add_field(name='?bitcoin', value='Sends the bitcoin value in USD.', inline=False)
		embed.add_field(name='?gif', value="Responds with the a random GIF!", inline=False)
		embed.add_field(name='?champlevel (player name)', value="Responds with the player's summoner level in League.", inline=False)
		embed.add_field(name='?leaguerank (player name)', value="Responds with the player's competitive rank in League.", inline=False)
		embed.add_field(name='?matchKDA ("player name")', value="Takes the summoner name in quotes then reponds with recent match KDA.", inline=False)
		embed.add_field(name='?MVPchamp ("player name")', value="Takes the summoner name in quotes then reponds with the most played champion in the last 50 matches.", inline=False)
		await client.send_message(message.channel, embed=embed)
	else:
		await client.process_commands(message)

@client.event #gang gang fun
async def on_message(message):
	if message.content.startswith('Gang gang'):
		await client.send_message(message.channel, 'Gang Gang :gun:')
	elif message.content.startswith('gang gang'):
		await client.send_message(message.channel, 'Gang Gang :gun:')
	elif message.content.startswith('ganggang'):
		await client.send_message(message.channel, 'Gang Gang :gun:')
	else:
		await client.process_commands(message)
	
		
@client.command()
async def bitcoin():
	url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
	response = requests.get(url)
	value = response.json()['bpi']['USD']['rate']
	await client.say('Bitcoin price is: $' + value)

@client.command()
async def champlevel(userID):
	url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+userID+'?api_key=RGAPI-ccad9aae-0ce2-4651-adee-d72d62ba43c5'
	response = requests.get(url)
	value = response.json()['summonerLevel']
	await client.say('Your summoner level is: ' + str(value))
	
@client.command(pass_context=True)
async def gif(ctx):
	urls = [
		'https://thumbs.gfycat.com/BowedIckyGreatargus-size_restricted.gif',
		'https://thumbs.gfycat.com/ForthrightHealthyBluefish-size_restricted.gif',
		'https://thumbs.gfycat.com/RegularCrazyAmericanwigeon-size_restricted.gif',
	]
	embed = discord.Embed()
	embed.set_image(url=random.choice(urls))
	await client.send_message(ctx.message.channel, embed=embed)
	
@client.command()
async def leaguerank(summonerName): #takes the player's name as parameter on discord cmd (space after cmd name)
	summonerID = nameToID(summonerName)
	url = 'https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/'+summonerID+'?api_key='+RIOTAPI #now grabs the ranked stats url and presents it
	response = requests.get(url) #sets a variable for the intake of the ranked stats
	value1 = response.json()[0]['tier'] #takes the zero'th section of the array presented by the json file and finds 'tier' within it
	value2 = response.json()[0]['rank'] #same thing but for 'rank' in the same section
	
	await client.say(summonerName + "'s rank is: " + (value1) + " " + (value2)) #sends a discord message with the summoner name, their rank and tier
	print('Looked up rank for ' + summonerName) #prints name to console

@client.command()
async def matchKDA(summonerName):
	nameToGameID(summonerName)
	KDAgameID = (gameID)
	searchforPlayer(summonerName, KDAgameID)
	#print(arraynum)
	correctarraynum = (arraynum)
	KDAurl = 'https://na1.api.riotgames.com/lol/match/v4/matches/'+gameID+'?api_key='+RIOTAPI
	KDAresponse = requests.get(KDAurl)
	grabKills = KDAresponse.json()['participants'][correctarraynum]['stats']['kills']
	grabDeaths = KDAresponse.json()['participants'][correctarraynum]['stats']['deaths']
	grabAssists = KDAresponse.json()['participants'][correctarraynum]['stats']['assists']
	Kills = str(grabKills)
	Deaths = str(grabDeaths)
	Assists = str(grabAssists)
	KDA = str(summonerName+"'s most recent match KDA was "+Kills+"/"+Deaths+"/"+Assists)
	await client.say(KDA)
	
@client.command()
async def MVPchamp(summonerName):
	nameToAccID(summonerName)
	MVPaccountID = accountID
	addChampCount(MVPaccountID)
	mostPlayedChampID = mostCommon[0]
	mpCIDstr = str(mostPlayedChampID)
	a,b = mpCIDstr.split(", ")
	anew = a.replace("(","")
	bnew = b.replace(")","")
	print(str(anew) + " is the ID for most played and it was played " + str(bnew) + " times.")
	gameverurl = 'https://ddragon.leagueoflegends.com/api/versions.json'
	GameverResponse = requests.get(gameverurl)
	grabGameVer = GameverResponse.json()[0]
	global GameVersion
	GameVersion = str(grabGameVer)
	#print(GameVersion + ": Game Version")
	anewint = int(anew)
	championName = num2words[anewint]
	newchampName = str(championName)
	print(newchampName)
	await client.say("In " + summonerName + "'s most recent 50 matches, the most frequently played champion is "+newchampName+" at a total of "+bnew+" times.")
	playeddivide = (int(bnew)/50)
	playedpercent = (playeddivide * 100)
	playedperstr = str(playedpercent)
	await client.say("The played percentage is " + playedperstr + "%.")

def addChampCount(accID):
	global champNum
	global mostCommon
	champNum = []
	matchNum = -1
	CCaccountID = str(accID)
	matchlisturl = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+CCaccountID+'?api_key='+RIOTAPI
	mlresponse = requests.get(matchlisturl)
	for x in range(49):
		matchNum += 1
		grabchampIDs = mlresponse.json()['matches'][int(matchNum)]['champion'] #need to put in loop for x number of games
		champNum.append(grabchampIDs)
		#print(champNum)
	count = Counter(champNum)
	mostCommon = count.most_common(1)
	print(count)
	#print(mostCommon)
	return mostCommon
		
	
def	nameToAccID(Name):
	accurl = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+Name+'?api_key='+RIOTAPI #presents the account ID url with the name as paramter for API
	accIDresponse = requests.get(accurl) #sets up the request intake so that values can be pulled from site
	grabaccountID = accIDresponse.json()['accountId'] #sets a different variable for the part of json text labeled as 'id'
	global accountID
	accountID = str(grabaccountID) #finally sets summonerID to the string form of the previous variable
	return accountID
	
def nameToGameID(Name):
	accurl = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+Name+'?api_key='+RIOTAPI #presents the account ID url with the name as paramter for API
	accIDresponse = requests.get(accurl) #sets up the request intake so that values can be pulled from site
	grabaccountID = accIDresponse.json()['accountId'] #sets a different variable for the part of json text labeled as 'id'
	accountID = str(grabaccountID) #finally sets summonerID to the string form of the previous variable
	matchlisturl = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+accountID+'?api_key='+RIOTAPI
	mlresponse = requests.get(matchlisturl)
	grabgameID = mlresponse.json()['matches'][0]['gameId']
	global gameID
	gameID = str(grabgameID)
	return gameID

def searchforPlayer(Name, ID):
	global arraynum
	arraynum = 0
	runwhile = 0
	matchurl = 'https://na1.api.riotgames.com/lol/match/v4/matches/'+ID+'?api_key='+RIOTAPI
	matchresponse = requests.get(matchurl)
	grabPiName = matchresponse.json()['participantIdentities'][arraynum]['player']['summonerName']
	PisummName = str(grabPiName)
	while (PisummName != Name and runwhile == 0):
		arraynum += 1
		newarraynum = int(arraynum)
		grabPiName = matchresponse.json()['participantIdentities'][newarraynum]['player']['summonerName']
		PisummName = str(grabPiName)
		#print("PisummName does not equal Name")
	if (PisummName == Name):
		runwhile = 1
		return arraynum

def nameToID(Name): #for summonerID
	idurl = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+Name+'?api_key='+RIOTAPI #presents the summoner ID url with the name as paramter for API
	IDresponse = requests.get(idurl) #sets up the request intake so that values can be pulled from site
	grabsummonerID = IDresponse.json()['id'] #sets a different variable for the part of json text labeled as 'id'
	global summonerID
	summonerID = str(grabsummonerID) #finally sets summonerID to the string form of the previous variable
	return summonerID #returns the variable for other function use

	#global champName
	#runWhile = True
	#champListNum = 0
	#NewGameVersion = GameVersion
	#champlisturl = 'https://ddragon.leagueoflegends.com/cdn/'+NewGameVersion+'/data/en_US/champion.json'
	#champlistResponse = requests.get(champlisturl)
	#grabChampList = champlistResponse.json()['data'][champListNum]
	#champNumber = str(grabChampList)
	#while (champNumber != champID and runWhile == True):
	#	champListNum += 1
	#	grabChampList = champlistResponse.json()['data'][champListNum]
	#	champNumber = str(grabChampList)
	#	print(champNumber + " champ Numbers")
	#if (champNumber == champID):
	#	runWhile = False
	#	champName = champlistResponse.json()['data'][champListNum]['key']
	#return champName
	
client.run(TOKEN)
