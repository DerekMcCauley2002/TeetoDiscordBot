import discord
import random
import requests
import json
#import gspread

from collections import Counter
from discord import Game
from discord.utils import get
from discord.ext.commands import Bot


BOT_PREFIX = ('?')
TOKEN = \
	"NTE1MjY4MTE0MDg3NDExNzEy.DtkKVQ.9Qx8N25CDzUkQ1CQe2agsM0KvaQ"
RIOTAPI = \
	'RGAPI-838186e9-3ba6-4085-9f3a-60638a7e00b5'
killpass = \
	"toenditall"

client = Bot(command_prefix=BOT_PREFIX)

client.remove_command('help')

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
			89: 'Leona', 90: 'Malzahar', 127: 'Lissandra', 555: 'Pyke', \
			91: 'Talon', 92: 'Riven', 136: 'Aurelion Sol', 60: 'Elise', \
			96: "Kog'Maw", 98: 'Shen', 121: "Kha'Zix", 133: 'Quinn', \
			99: 'Lux', 101: 'Xerath', 102: 'Shyvana', \
			103: 'Ahri', 104: 'Graves', 105: 'Fizz', 106: 'Volibear', \
			107: 'Rengar', 110: 'Varus', 134: 'Syndra', 141: 'Kayn', \
			111: 'Nautilus', 112: 'Viktor', 113: 'Sejuani', 114: 'Fiora', \
			115: 'Ziggs', 117: 'Lulu', \
			119: 'Draven', 120: 'Hecarim', 122: 'Darius', \
			126: 'Jayce', 142: 'Zoe', \
			131: 'Diana', 518: 'Neeko', \
			143: 'Zyra', 145: "Kai'Sa", \
			516: 'Ornn', 498: 'Xayah', 497: 'Rakan', 150: 'Gnar', \
			432: 'Bard', 429: 'Kalista', 427: 'Ivern', 154: 'Zac', \
			421: "Rek'Sai", 420: 'Illaoi', 157: 'Yasuo', 412: 'Thresh', \
			268: 'Azir', 267: 'Nami', 161: "Velkoz", 266: 'Aatrox', \
			163: 'Taliyah', 164: 'Camille', 201: "Braum", 202: 'Jhin', \
			203: 'Kindred', 222: 'Jinx', 223: 'Tahm Kench', 236: 'Lucian', \
			238: 'Zed', 240: 'Kled', 245: 'Ekko', 254: 'Vi'}

@client.event
async def on_ready(): #startup code
	await client.change_presence(game=Game(name="?help"))
	print('Logged in as ' + client.user.name)

@client.command(pass_context=True)
async def killbot(ctx, password):
	if (password == killpass):
		await client.send_message(ctx.message.channel, "fill stub")
		async for x in client.logs_from(ctx.message.channel, limit = number + 1):
			mgs.append(x)
		await client.delete_messages(mgs)
		await client.send_message(ctx.message.channel, embed=embed)
		quit()

@client.command(pass_context=True)
async def help(ctx, dm = "user"):
	embed = discord.Embed(
		title='Teeto Bot Help',
		description='Description of all current commands.',
		color=0xc45100
	)
	embed.add_field(name='?**champlevel** ("player name")', value="Responds with the player's summoner level in League. \n Aliases: *slvl* | *userlvl*", inline=False)
	embed.add_field(name='?**leaguerank** ("player name")', value="Responds with the player's competitive rank in League. \n Alias: *rank*", inline=False)
	embed.add_field(name='?**matchKDA** ("player name")', value="Takes the summoner name in quotes then reponds with recent match KDA. \n Alias: *kda*", inline=False)
	embed.add_field(name='?**MVPchamp** ("player name")', value="Takes the summoner name in quotes then reponds with the most played champion in the last 50 matches. \n Alias: *mvp*", inline=False)
	embed.add_field(name='?**MVPlast** ("player name") (matches to count)', value= "Takes the summoner name in quotes then reponds with the most played champion in the last X matches. \n Alias: *mvpl*", inline=False)
	embed.add_field(name='?**fives** (Game Role) ("role to mention")', value= 'Messages the selected role and opens a poll type response with reactions to organize a full team. \
	\n Potential `Game Roles` are: **Top, Jungle, Mid, ADC, & Support**', inline=False)
	
	mgs = []
	number = int(1)
	await client.send_message(ctx.message.channel, "fill stub")
	if (dm == "chat"):
		async for x in client.logs_from(ctx.message.channel, limit = number + 1):
			mgs.append(x)
		await client.delete_messages(mgs)
		await client.send_message(ctx.message.channel, embed=embed)
	else:
		async for x in client.logs_from(ctx.message.channel, limit = number + 1):
			mgs.append(x)
		await client.delete_messages(mgs)
		await client.send_message(ctx.message.author, embed=embed)
	
@client.command(pass_context=True)
async def clear(ctx, number):
	mgs = [] #Empty list to put all the messages in the log
	number = int(number) #Converting the amount of messages to delete to an integer
	async for x in client.logs_from(ctx.message.channel, limit = number + 1):
		mgs.append(x)
	await client.delete_messages(mgs)

@client.command()
async def gamerole(role):
	global gameRole
	gameRole = role
	return gameRole

@client.command(pass_context=True)
async def fives(ctx, role='Fill', ping="None"):
	canTop = True
	canJG = True
	canMid = True
	canBot = True
	canSupp = True
	Top = ':Top:529761810279038977'
	Jungle = ':Jungle:529761832756576266'
	Middle = ':Middle:529761843598852096'
	Bottom = ':Bottom:529761862158647307'
	Support = ':Support:529761870987657218'
	
	pingRole = discord.utils.get(ctx.message.channel.server.roles, name="{}".format(ping))
		if (role=="Top" or role=="top"):
		role=Top
		taken = "*`Top`* is their preferred role."
		canTop = False
	elif (role=="Middle" or role=="Mid" or role=="mid"):
		role=Middle
		taken = "*`Mid`* is their preferred role."
		canMid = False
	elif (role=="Jungle" or role=="Jg" or role=="jg"):
		role=Jungle
		taken = "*`Jungle`* is their preferred role."
		canJG = False
	elif (role=="Bottom" or role=="Bot" or role=="bot" or role=="ADC" or role=="adc"):
		role=Bottom
		taken = "*`ADC`* is their preferred role."
		canBot = False
	elif (role=="Support" or role=="Supp" or role=="supp"):
		role=Support
		taken = "*`Support`* is their preferred role."
		canSupp = False
	elif (role=="Fill"):
		taken = "They are willing to *`fill`* or have no preselected role."
		
	embed = discord.Embed(
		title='Join me in a five stack game!',
		description='*`{}`* is looking for other players to join. \n Select the role from the reactions above!'.format(ctx.message.author.name),
		color=0xc45100
	)
	embed.add_field(name="Occupied Role", value=taken, inline=False)
	await client.send_message(ctx.message.channel, embed=embed)
	
	if (canTop == True):
		await client.add_reaction(ctx.message,Top)
	if (canJG == True):
		await client.add_reaction(ctx.message,Jungle)
	if (canMid == True):
		await client.add_reaction(ctx.message,Middle)
	if (canBot == True):
		await client.add_reaction(ctx.message,Bottom)
	if (canSupp == True):
		await client.add_reaction(ctx.message,Support)
	await client.send_message(ctx.message.channel, "" + pingRole.mention)

@client.command(aliases=['playchamp'])
async def shouldI():
	possible_responses = [
		'Yes you should do that crazy build.',
		'No, that matchup sucks.',
		'Full Send Brother!',
		"Don't play that champ, they kinda suck.",
		"That's a lot of bm, but I like it... do it!",
	]
	await client.say(random.choice(possible_responses))

@client.command(pass_context = True, aliases=['slvl', 'userlvl'])
async def summlevel(ctx, summonerName):
	summNameInput = str(summonerName)
	url = 'https://na1.api.riotgames.com/lol/summoner/v3/summoners/by-name/'+summonerName+'?api_key=' + RIOTAPI
	response = requests.get(url)
	value = response.json()['summonerLevel']
	await client.say('Your summoner level is: ' + str(value))
	
@client.command(pass_context = True, aliases=['rank'])
async def leaguerank(ctx, summonerName): #takes the player's name as parameter on discord cmd (space after cmd name)
	summNameInput = str(summonerName)
	summonerID = nameToID(summonerName)
	url = 'https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/'+summonerID+'?api_key='+RIOTAPI #now grabs the ranked stats url and presents it
	response = requests.get(url) #sets a variable for the intake of the ranked stats
	value1 = response.json()[0]['tier'] #takes the zero'th section of the array presented by the json file and finds 'tier' within it
	value2 = response.json()[0]['rank'] #same thing but for 'rank' in the same section
	
	await client.say(summonerName + "'s rank is: " + (value1) + " " + (value2)) #sends a discord message with the summoner name, their rank and tier
	print('Looked up rank for ' + summonerName) #prints name to console

@client.command(pass_context = True, aliases=['kda'])
async def matchKDA(ctx, summonerName):
	summNameInput = str(summonerName)
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
	nameToAccID(summonerName)
	newAccID = str(accountID)
	matchlisturl = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+newAccID+'?api_key='+RIOTAPI
	mlresponse = requests.get(matchlisturl)
	grabchampIDs = mlresponse.json()['matches'][0]['champion']
	recentChampNum = int(grabchampIDs)
	recentChampName = num2words[recentChampNum]
	rCNstr = str(recentChampName)
	KDA = str(summonerName+"'s most recent match KDA was "+Kills+"/"+Deaths+"/"+Assists+" on "+rCNstr)
	await client.say(KDA)
	
@client.command(pass_context = True, aliases=['mvp'])
async def MVPchamp(ctx, summonerName):
	summNameInput = str(summonerName)
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
	playedpercentrnd = round(playedpercent, 2)
	playedperstr = str(playedpercentrnd)
	await client.say("The played percentage is " + playedperstr + "%.")

@client.command(pass_context = True, aliases=['mvpl'])
async def MVPlast(ctx, summonerName, range):
	summNameInput = str(summonerName)
	nameToAccID(summonerName)
	MVPaccountID = accountID
	newrange = int(range)
	addChampCountRange(MVPaccountID, newrange)
	mvplastrange = functrange
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
	mvplastrangestr = str(mvplastrange)
	await client.say("In " + summonerName + "'s most recent " + mvplastrangestr + " matches, the most frequently played champion is "+newchampName+" at a total of "+bnew+" times.")
	playeddivide = (int(bnew)/mvplastrange)
	playedpercent = (playeddivide * 100)
	playedpercentrnd = round(playedpercent, 2)
	playedperstr = str(playedpercentrnd)
	await client.say("The played percentage is " + playedperstr + "%.")
	
def matchname(discordUser):
	rowsearchnum = 1
	discordnameCheck = sheet.row_values(rowsearchnum)
	discordnameSet = discordnameCheck[0]
	while (discordnameSet != discordUser):
		rowsearchnum +=1
		discordnameCheck = sheet.row_values(rowsearchnum)
		discordnameSet = discordnameCheck[0]
	if (discordnameSet == discordUser):
		summNameSet = sheet.row_values(rowsearchnum)
	global newSummName
	newSummName = str(summNameSet[1])
	return newSummName

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

def addChampCountRange(accID, inrange):
	global champNum
	global mostCommon
	global functrange
	functrange = inrange
	champNum = []
	matchNum = -1
	CCaccountID = str(accID)
	matchlisturl = 'https://na1.api.riotgames.com/lol/match/v4/matchlists/by-account/'+CCaccountID+'?api_key='+RIOTAPI
	mlresponse = requests.get(matchlisturl)
	for x in range(functrange):
		matchNum += 1
		grabchampIDs = mlresponse.json()['matches'][int(matchNum)]['champion'] #need to put in loop for x number of games
		champNum.append(grabchampIDs)
		#print(champNum)
	count = Counter(champNum)
	mostCommon = count.most_common(1)
	print(count)
	#print(mostCommon)
	return mostCommon
	return functrange
	
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
	
client.run(TOKEN)