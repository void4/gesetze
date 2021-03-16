from glob import glob
from bs4 import BeautifulSoup
from wordcloud import WordCloud

paths = glob("xml/*.xml")

alltext = ""

print(len(paths))

for i, path in enumerate(paths):#[:10]
	#print(i)
	with open(path) as f:
		soup = BeautifulSoup(f.read(), "xml")
		#kurzue = soup.find("kurzue").text
		langue = soup.find("langue").text
		abk = soup.find("jurabk").text#amtabk
		ausf = soup.find("ausfertigung-datum").text
		text = "\n".join(soup.findAll(text=True))
		if "Test" in text:
			print(i, ausf, abk, langue, path)
		
