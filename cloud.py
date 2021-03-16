from glob import glob
from bs4 import BeautifulSoup
from wordcloud import WordCloud

paths = glob("xml/*.xml")

alltext = ""

print(len(paths))

for i, path in enumerate(paths):#[:10]
	print(i)
	with open(path) as f:
		soup = BeautifulSoup(f.read(), "xml")
		#kurzue = soup.find("kurzue").text
		langue = soup.find("langue").text
		
		text = "\n".join(soup.findAll(text=True))
		#print(text)
		
		alltext += text
		
wordcloud = WordCloud(width=1920, height=1080).generate(alltext)
#print(dir(wordcloud))
wordcloud.to_image().save("cloud.png")
