from string import ascii_uppercase, digits
from bs4 import BeautifulSoup
import requests
from time import sleep
import os
import urllib.request
import urllib.parse as urlparse

os.makedirs("pdf", exist_ok=True)

a1 = ascii_uppercase + digits

for letter in a1:
	page = requests.get(f"https://www.gesetze-im-internet.de/Teilliste_{letter}.html").text
	soup = BeautifulSoup(page, "html.parser")
	div = soup.find("div", {"id":"paddingLR12"})
	
	if div is None:
		continue
	
	for link in div.findAll("a"):
		if link["href"].endswith(".pdf"):
			
			curr_link = "http://www.gesetze-im-internet.de/" + link["href"][2:]
			parsed_link = urlparse.urlsplit(curr_link)
			parsed_link = parsed_link._replace(path=urlparse.quote(parsed_link.path))
			encoded_link = parsed_link.geturl()
			print(encoded_link)
			urllib.request.urlretrieve(encoded_link, "pdf/"+link["href"].split("/")[-1])
			sleep(0.1)
	#os.system()
