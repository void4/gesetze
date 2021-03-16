from string import ascii_uppercase, digits
from bs4 import BeautifulSoup
import requests
from time import sleep
from zipfile import ZipFile, BadZipFile
from io import BytesIO
import os

os.makedirs("xml", exist_ok=True)

a1 = ascii_uppercase + digits

for letter in a1:
	page = requests.get(f"https://www.gesetze-im-internet.de/Teilliste_{letter}.html").text
	soup = BeautifulSoup(page, "html.parser")
	div = soup.find("div", {"id":"paddingLR12"})
	
	if div is None:
		continue
	
	for link in div.findAll("a"):
		if link["href"].endswith("index.html"):
			gesetz = link["href"].rsplit("/", 1)[0][2:]
			print(letter, gesetz)
			xmlurl = "https://www.gesetze-im-internet.de/" + gesetz + "/xml.zip"
			try:
				xmlzip = ZipFile(BytesIO(requests.get(xmlurl).content))
			except BadZipFile:
				continue
	
			for zipfile in xmlzip.infolist():
				xmlzip.extract(zipfile, "xml")
			sleep(0.1)
	#os.system()
