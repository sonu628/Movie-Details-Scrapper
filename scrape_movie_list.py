from bs4 import BeautifulSoup
import time
import requests
from sys import argv

script, amount = argv
num = int(argv[1])
x = 1
while x <= num:
	url = ("http://123movies.net/recently-added/page-%s.html" %x)
	data = requests.get(url)
	data = data.text
	soup = BeautifulSoup(data, "html.parser")

	items = soup.find_all("div",{"class":"ml-item"})
	for s in items:
		bb = s.find("a").get("href")
		#print(bb)
		over = s.find("a").get("onmouseover")
		if "Season" in over:
			pass
		else:
			print(bb)
			with open("movies_list.txt", "a") as file:
				file.write(bb+"\n")
				file.close()

	x+=1
