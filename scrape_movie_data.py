from bs4 import BeautifulSoup
import time
import requests
from requests import get
import re
# from importlib import reload

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import base64

lines = [line.strip() for line in open('movies_list.txt')]



def year_pattern(text):
	if len(text) != 4:
		return False
	for i in range(0,4):
		if not text[i].isdigit():
			return False
	return True

x = 0

for l in lines:
	#try:
	url = lines[x]
	data = requests.get(url)
	data = data.text  # deleting tags
	soup = BeautifulSoup(data, "html.parser")
	
	
	data = requests.get(url)
	data = data.text  # deleting tags
	print(data)
	try:
		titlePath = soup.find_all("div",{"class":"mvic-desc"})
		for l in titlePath:
			title = l.find("h3")
			title = title.text
			print("title is "+title)
			# delete year from title
			for i in range(len(title)):
				year = title[i:i+4]
				if year_pattern(year):
					delete_year = title.split(("("),1)[0]
					title = delete_year
				else:
					title = title
	except:
		title = "[[none]]"
		pass
	print(title)
	
	#poster movie image
	try:
		image = soup.find("meta",{"property":"og:image"}).get("content")
	except:
		image = "[[none]]"
		pass
	#print(image)
	#description
	try:
		desc = soup.find("div", {"class":"desc"})
		desc = desc.text
		description = desc.strip("\n")
		description = description.rstrip()
		description = description.lstrip()
		#print(description)
	except:
		description = "[[none]]"
		pass
				
	#movie genres
	try:
		genres1 = soup.find("div",{"class":"mvici-left"})
		genres2 = genres1.find("p")
		genres3 = genres2.find("a")
		genres = genres3.text
	except:
		genres = "[[none]]"
		pass
	#print(genres)
	
	#actors
	try:
		act1 = genres1.find_all("p")[1]
		actors = act1.find("a")
		actors = actors.text
	except:
		actors = "[[none]]"
		pass
	
	#director
	try:
		dir1 = genres1.find_all("p")[2]
		director = dir1.find("a")
		director = director.text
	except:
		director = "[[none]]"
		pass
	#print(director.text)
	
	#country
	try:
		cou1 = genres1.find_all("p")[3]
		country = cou1.find("a")
		country = country.text
		country = country.replace("USA", "United States")
		country = country.replace("UK", "United Kingdom")
	except:
		country = "[[none]]"
		pass
	#print(country.text)
	
	
	#right mvici
	right = soup.find("div", {"class":"mvici-right"})
	
	try:
		movie = right.find_all("p")[0]
		movie = movie.text
	except:
		movie = "[[none]]"
		pass
	#print(movie)
	
	#prod
	try:
		prod = right.find_all("p")[1]
		prod = prod.text
	except:
		prod = "[[none]]"
		pass
	#print(prod)
	
	#duration
	try:
		duration = right.find_all("p")[2]
		duration = duration.text
	except:
		duration = "[[none]]"
		pass
	#print(duration)
	
	#release
	try:
		release = right.find_all("p")[3]
		release = release.text
	except:
		release = "[[none]]"
		pass
	#print(release)
	#
	try:
		year = release.replace("Release: ","")
	except:
		year = "[[none]]"
		pass
	#print(year)
		
	#embed link
	#nie dziala
	try:
		embed1 = soup.find("div", {"id":"media-player"})
		emb = soup.find_all("iframe")

		coded_string = embed1.find("script")
		wtf = str(coded_string)
		line = wtf
		pat = r'decode([^&]+?)"[)][)]'
		
		decodeString = re.search(pat,line).group(1)
		
		#print(result.group(1))
		fff = base64.b64decode(decodeString)
		pattern = r'src="([^&]+?)"'
		ggg = str(fff)
		extractembed = re.search(pattern, ggg).group(1)
		#print(extractembed)
	except:
		extractembed = "[[none]]"
		pass
	
	#mirror
	
	try:
		mirror22 = soup.find_all("div",{"class":"server_line"})
		#print("boo1")
		for c in mirror22:
			ble = c.find("p",{"class":"server_servername"})
			dupa = ble.text
			if "OpenLoad" in dupa:
				oki = c.find("p",{"class":"server_play"})
		link22 = oki.find("a").get("href")
		url = link22
		""""""""""""""""""""""""""""""""""""
		""""""""""""""""""""""""""""""""""""
		""""""""""""""""""""""""""""""""""""
		data22 = requests.get(url)
		data22 = data22.text  # deleting tags
		#opener = AppURLopener()
		#data = opener.open(url)
		soup22 = BeautifulSoup(data22, "html.parser")
		#print("bi")
		try:
			embed1 = soup22.find("div", {"id":"media-player"})
			emb = soup.find_all("iframe")

			coded_string = embed1.find("script")
			wtf = str(coded_string)
			line = wtf
			pat = r'decode([^&]+?)"[)][)]'
			
			decodeString = re.search(pat,line).group(1)
			
			#print(result.group(1))
			fff = base64.b64decode(decodeString)
			pattern = r'src="([^&]+?)"'
			ggg = str(fff)
			extractembed2 = re.search(pattern, ggg).group(1)
			#print(extractembed)
		except:
			extractembed2 = "[[none]]"
			pass
		
				
	except:
		extractembed2 = "[[none]]"
		pass

	
	
	#mirror 2 - dzialajacy
	try:
		mirror22 = soup.find_all("div",{"class":"server_line"})
		#print("boo1")
		for c in mirror22:
			ble = c.find("p",{"class":"server_servername"})
			dupa = ble.text
			if "TheVideo" in dupa:
				oki = c.find("p",{"class":"server_play"})
		link22 = oki.find("a").get("href")
		url = link22
		""""""""""""""""""""""""""""""""""""
		""""""""""""""""""""""""""""""""""""
		""""""""""""""""""""""""""""""""""""
		data22 = requests.get(url)
		data22 = data22.text  # deleting tags
		#opener = AppURLopener()
		#data = opener.open(url)
		soup22 = BeautifulSoup(data22, "html.parser")
		#print("bi")
		try:
			embed1 = soup22.find("div", {"id":"media-player"})
			emb = soup.find_all("iframe")

			coded_string = embed1.find("script")
			wtf = str(coded_string)
			line = wtf
			pat = r'decode([^&]+?)"[)][)]'
			
			decodeString = re.search(pat,line).group(1)
			
			#print(result.group(1))
			fff = base64.b64decode(decodeString)
			pattern = r'src="([^&]+?)"'
			ggg = str(fff)
			extractembed3 = re.search(pattern, ggg).group(1)
			#print(extractembed)
		except:
			extractembed3 = "[[none]]"
			pass
	except:
		extractembed3 = "[[none]]"
	
	
	output_ = "%s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s ## %s !! %s !! %s" % (year, title, description, genres, actors, director, country, movie, prod, duration, release, image, extractembed,extractembed2, extractembed3)
	with open("123net_f.txt", "a") as file:
		file.write(output_+"\n")
		file.close()
		print(output_)
	x+=1
	#except:
	#	print("error")
	#	x+=1
	#	pass
		
	
