from glob import glob
from bs4 import BeautifulSoup
from multiprocessing import Pool

paths = glob("xml/*.xml")

def analyze(path):

	with open(path) as f:
		#soup = BeautifulSoup(f.read(), "xml")
		soup = f.read()
		print(len(soup))
		#kurzue = soup.find("kurzue").text
		#langue = soup.find("langue").text
		#print(langue)
		#text = "\n".join(soup.findAll(text=True))
		#print(text)
		
with Pool(8) as pool:
	pool.map(analyze, paths)

		
