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
	if(message.content.startswith("?abathur")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Abathur'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?alarak")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Alarak'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?anub")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Anub\'arak'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?artanis")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Artanis'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?arthas")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Arthas'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?auriel")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Auriel'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?azmodan")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Azmodan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?brightwing")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Brightwing'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?butcher")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The%20Butcher'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?cassia")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cassia'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?chen")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chen'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?cho")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Cho'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?chromie")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Chromie'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?dva")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=D.Va'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?dehaka")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Dehaka'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?diablo")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Diablo'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?etc")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=E.T.C.'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?falstad")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Falstad'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?garrosh")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Garrosh'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?gazlowe")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gazlowe'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?genji")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Genji'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?greymane")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Greymane'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?guldan")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Gul\'dan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?illidan")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Illidan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?jaina")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Jaina'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?johanna")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Johanna'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?kt")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kael\'thas'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?kerrigan")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kerrigan'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?khara")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Kharazim'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?leoric")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Leoric'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?lili")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li Li'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?liming")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Li-Ming'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?morales")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lt. Morales'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?lunara")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Lunara'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?lucio")):
		url = 'https://goo.gl/4spScG' #Link shortened due to special character encoding issue.
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?malf")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malfurion'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?malth")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Malthael'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?medivh")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Medivh'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?muradin")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Muradin'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?murky")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Murky'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?naz")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nazeebo'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?nova")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Nova'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?probius")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Probius'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?rag")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Ragnaros'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?raynor")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Raynor'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?rehgar")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rehgar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?rexxar")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Rexxar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?samuro")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Samuro'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?hammer")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sgt. Hammer'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?sonya")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sonya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?stitches")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stitches'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?stukov")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Stukov'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?sylv")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Sylvanas'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?tass")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tassadar'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?vikings")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=The Lost Vikings'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?thrall")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Thrall'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?tracer")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tracer'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?tychus")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tychus'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?tyrael")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrael'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?tyrande")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Tyrande'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?uther")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Uther'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?valeera")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valeera'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?valla")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Valla'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?varian")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Varian'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?xul")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Xul'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?zagara")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zagara'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?zarya")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zarya'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?zeratul")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zeratul'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

	if(message.content.startswith("?zuljin")):
		url = 'https://www.hotslogs.com/Sitewide/HeroDetails?Hero=Zul\'jin'
		page = urlopen(url)

		soup = BeautifulSoup(page, 'html.parser')
		soup.title.string
		popularBuild = soup.find('tr', id='ctl00_MainContent_RadGridPopularTalentBuilds_ctl00__0')

		tags = []
		talents = popularBuild.findAll('img')
		for img in talents:
			if 'alt' in img.attrs:
				tags.append(img.attrs['alt'])	

		print (soup.title.string)
		for txt in tags:
			await client.send_message(message.channel, txt )
			print (txt)

client.run("")
