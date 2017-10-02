import discord
from discord.ext.commands import Bot
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup

Client = discord.Client()
bot_prefix="?"
client = commands.Bot(command_prefix = bot_prefix)

@client.event
async def on_ready():
	print ("Bot Online!")
	print ("Name: {}".format(client.user.name))
	print ("ID: {}".format(client.user.id))
	await client.change_presence(game=discord.Game(name='Heroes of the Storm'))

@client.event
async def on_message(message):
	if(message.content.startswith("?weak abathur")):
		url = 'https://www.heroescounters.com/hero/abathur'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak alarak")):
		url = 'https://www.heroescounters.com/hero/alarak'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak anubarak")):
		url = 'https://www.heroescounters.com/hero/anubarak'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak artanis")):
		url = 'https://www.heroescounters.com/hero/artanis'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak arthas")):
		url = 'https://www.heroescounters.com/hero/arthas'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak auriel")):
		url = 'https://www.heroescounters.com/hero/auriel'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak azmodan")):
		url = 'https://www.heroescounters.com/hero/azmodan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak brightwing")):
		url = 'https://www.heroescounters.com/hero/brightwing'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak cassia")):
		url = 'https://www.heroescounters.com/hero/cassia'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak chen")):
		url = 'https://www.heroescounters.com/hero/chen'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak chogall")):
		url = 'https://www.heroescounters.com/hero/chogall'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak chromie")):
		url = 'https://www.heroescounters.com/hero/chromie'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak dva")):
		url = 'https://www.heroescounters.com/hero/dva'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak dehaka")):
		url = 'https://www.heroescounters.com/hero/dehaka'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak diablo")):
		url = 'https://www.heroescounters.com/hero/diablo'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak etc")):
		url = 'https://www.heroescounters.com/hero/etc'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak falstad")):
		url = 'https://www.heroescounters.com/hero/falstad'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak garrosh")):
		url = 'https://www.heroescounters.com/hero/garrosh'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak gazlowe")):
		url = 'https://www.heroescounters.com/hero/gazlowe'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak genji")):
		url = 'https://www.heroescounters.com/hero/genji'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak greymane")):
		url = 'https://www.heroescounters.com/hero/greymane'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak guldan")):
		url = 'https://www.heroescounters.com/hero/guldan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak illidan")):
		url = 'https://www.heroescounters.com/hero/illidan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak jaina")):
		url = 'https://www.heroescounters.com/hero/jaina'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak johanna")):
		url = 'https://www.heroescounters.com/hero/johanna'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak kt")):
		url = 'https://www.heroescounters.com/hero/kaelthas'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak kerrigan")):
		url = 'https://www.heroescounters.com/hero/kerrigan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak monk")):
		url = 'https://www.heroescounters.com/hero/kharazim'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak leoric")):
		url = 'https://www.heroescounters.com/hero/leoric'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak lili")):
		url = 'https://www.heroescounters.com/hero/lili'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak liming")):
		url = 'https://www.heroescounters.com/hero/li-ming'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak morales")):
		url = 'https://www.heroescounters.com/hero/ltmorales'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak lucio")):
		url = 'https://www.heroescounters.com/hero/lucio'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak lunara")):
		url = 'https://www.heroescounters.com/hero/lunara'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak malf")):
		url = 'https://www.heroescounters.com/hero/malfurion'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak malth")):
		url = 'https://www.heroescounters.com/hero/malthael'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak medivh")):
		url = 'https://www.heroescounters.com/hero/medivh'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak muradin")):
		url = 'https://www.heroescounters.com/hero/muradin'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak murky")):
		url = 'https://www.heroescounters.com/hero/murky'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak nazeebo")):
		url = 'https://www.heroescounters.com/hero/nazeebo'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak nova")):
		url = 'https://www.heroescounters.com/hero/nova'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak probius")):
		url = 'https://www.heroescounters.com/hero/probius'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak ragnaros")):
		url = 'https://www.heroescounters.com/hero/ragnaros'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak raynor")):
		url = 'https://www.heroescounters.com/hero/raynor'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak rehgar")):
		url = 'https://www.heroescounters.com/hero/rehgar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak rexxar")):
		url = 'https://www.heroescounters.com/hero/rexxar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak samuro")):
		url = 'https://www.heroescounters.com/hero/samuro'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak hammer")):
		url = 'https://www.heroescounters.com/hero/sgthammer'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak sonya")):
		url = 'https://www.heroescounters.com/hero/sonya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak stitches")):
		url = 'https://www.heroescounters.com/hero/stitches'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak stukov")):
		url = 'https://www.heroescounters.com/hero/stukov'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak sonya")):
		url = 'https://www.heroescounters.com/hero/sonya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak tassadar")):
		url = 'https://www.heroescounters.com/hero/tassadar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak butcher")):
		url = 'https://www.heroescounters.com/hero/thebutcher'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak vikings")):
		url = 'https://www.heroescounters.com/hero/thelostvikings'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak thrall")):
		url = 'https://www.heroescounters.com/hero/thrall'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak tracer")):
		url = 'https://www.heroescounters.com/hero/tracer'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak tychus")):
		url = 'https://www.heroescounters.com/hero/tychus'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak tyrael")):
		url = 'https://www.heroescounters.com/hero/tyrael'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak tyrande")):
		url = 'https://www.heroescounters.com/hero/tyrande'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak uther")):
		url = 'https://www.heroescounters.com/hero/uther'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak valeera")):
		url = 'https://www.heroescounters.com/hero/valeera'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak valla")):
		url = 'https://www.heroescounters.com/hero/valla'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak varian")):
		url = 'https://www.heroescounters.com/hero/varian'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak xul")):
		url = 'https://www.heroescounters.com/hero/xul'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak zagara")):
		url = 'https://www.heroescounters.com/hero/zagara'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak zarya")):
		url = 'https://www.heroescounters.com/hero/zarya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak zeratul")):
		url = 'https://www.heroescounters.com/hero/zeratul'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?weak zuljin")):
		url = 'https://www.heroescounters.com/hero/zuljin'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-bad')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong abathur")):
		url = 'https://www.heroescounters.com/hero/abathur'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong alarak")):
		url = 'https://www.heroescounters.com/hero/alarak'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong anubarak")):
		url = 'https://www.heroescounters.com/hero/anubarak'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong artanis")):
		url = 'https://www.heroescounters.com/hero/artanis'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong arthas")):
		url = 'https://www.heroescounters.com/hero/arthas'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong auriel")):
		url = 'https://www.heroescounters.com/hero/auriel'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong azmodan")):
		url = 'https://www.heroescounters.com/hero/azmodan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong brightwing")):
		url = 'https://www.heroescounters.com/hero/brightwing'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong cassia")):
		url = 'https://www.heroescounters.com/hero/cassia'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong chen")):
		url = 'https://www.heroescounters.com/hero/chen'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong chogall")):
		url = 'https://www.heroescounters.com/hero/chogall'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong chromie")):
		url = 'https://www.heroescounters.com/hero/chromie'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong dva")):
		url = 'https://www.heroescounters.com/hero/dva'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong dehaka")):
		url = 'https://www.heroescounters.com/hero/dehaka'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong diablo")):
		url = 'https://www.heroescounters.com/hero/diablo'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong etc")):
		url = 'https://www.heroescounters.com/hero/etc'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong falstad")):
		url = 'https://www.heroescounters.com/hero/falstad'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong garrosh")):
		url = 'https://www.heroescounters.com/hero/garrosh'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong gazlowe")):
		url = 'https://www.heroescounters.com/hero/gazlowe'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong genji")):
		url = 'https://www.heroescounters.com/hero/genji'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong greymane")):
		url = 'https://www.heroescounters.com/hero/greymane'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong guldan")):
		url = 'https://www.heroescounters.com/hero/guldan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong illidan")):
		url = 'https://www.heroescounters.com/hero/illidan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong jaina")):
		url = 'https://www.heroescounters.com/hero/jaina'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong johanna")):
		url = 'https://www.heroescounters.com/hero/johanna'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong kt")):
		url = 'https://www.heroescounters.com/hero/kaelthas'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong kerrigan")):
		url = 'https://www.heroescounters.com/hero/kerrigan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong monk")):
		url = 'https://www.heroescounters.com/hero/kharazim'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong leoric")):
		url = 'https://www.heroescounters.com/hero/leoric'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong lili")):
		url = 'https://www.heroescounters.com/hero/lili'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong liming")):
		url = 'https://www.heroescounters.com/hero/li-ming'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong morales")):
		url = 'https://www.heroescounters.com/hero/ltmorales'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong lucio")):
		url = 'https://www.heroescounters.com/hero/lucio'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong lunara")):
		url = 'https://www.heroescounters.com/hero/lunara'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong malf")):
		url = 'https://www.heroescounters.com/hero/malfurion'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong malth")):
		url = 'https://www.heroescounters.com/hero/malthael'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong medivh")):
		url = 'https://www.heroescounters.com/hero/medivh'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong muradin")):
		url = 'https://www.heroescounters.com/hero/muradin'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong murky")):
		url = 'https://www.heroescounters.com/hero/murky'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong nazeebo")):
		url = 'https://www.heroescounters.com/hero/nazeebo'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong nova")):
		url = 'https://www.heroescounters.com/hero/nova'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong probius")):
		url = 'https://www.heroescounters.com/hero/probius'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong ragnaros")):
		url = 'https://www.heroescounters.com/hero/ragnaros'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong raynor")):
		url = 'https://www.heroescounters.com/hero/raynor'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong rehgar")):
		url = 'https://www.heroescounters.com/hero/rehgar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong rexxar")):
		url = 'https://www.heroescounters.com/hero/rexxar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong samuro")):
		url = 'https://www.heroescounters.com/hero/samuro'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong hammer")):
		url = 'https://www.heroescounters.com/hero/sgthammer'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong sonya")):
		url = 'https://www.heroescounters.com/hero/sonya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong stitches")):
		url = 'https://www.heroescounters.com/hero/stitches'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong stukov")):
		url = 'https://www.heroescounters.com/hero/stukov'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong sonya")):
		url = 'https://www.heroescounters.com/hero/sonya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong tassadar")):
		url = 'https://www.heroescounters.com/hero/tassadar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong butcher")):
		url = 'https://www.heroescounters.com/hero/thebutcher'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong vikings")):
		url = 'https://www.heroescounters.com/hero/thelostvikings'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong thrall")):
		url = 'https://www.heroescounters.com/hero/thrall'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong tracer")):
		url = 'https://www.heroescounters.com/hero/tracer'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong tychus")):
		url = 'https://www.heroescounters.com/hero/tychus'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong tyrael")):
		url = 'https://www.heroescounters.com/hero/tyrael'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong tyrande")):
		url = 'https://www.heroescounters.com/hero/tyrande'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong uther")):
		url = 'https://www.heroescounters.com/hero/uther'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong valeera")):
		url = 'https://www.heroescounters.com/hero/valeera'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong valla")):
		url = 'https://www.heroescounters.com/hero/valla'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong varian")):
		url = 'https://www.heroescounters.com/hero/varian'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong xul")):
		url = 'https://www.heroescounters.com/hero/xul'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong zagara")):
		url = 'https://www.heroescounters.com/hero/zagara'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong zarya")):
		url = 'https://www.heroescounters.com/hero/zarya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong zeratul")):
		url = 'https://www.heroescounters.com/hero/zeratul'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

	if(message.content.startswith("?strong zuljin")):
		url = 'https://www.heroescounters.com/hero/zuljin'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('ul',class_='counterlist counterlist-good')

		count = 0
		for link in popularBuild.findAll('a'):
			count+=1
			if count %2 == 0 and count < 11:
				print(link.string)
				await client.send_message(message.channel, link.string)

client.run("")
