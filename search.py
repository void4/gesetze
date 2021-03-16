from glob import glob
from bs4 import BeautifulSoup
import xml.etree.cElementTree as ET
from collections import Counter

paths = glob("xml/*.xml")

counter = Counter()

repl = ".,;()"

def replace(text):
	result = ""
	for c in text:
		if c not in repl:
			result += c
		else:
			result += " "
	return result

try:
	for path in paths:

		tree = ET.parse(path) 
		text = ET.tostring(tree.getroot(), encoding='utf-8', method='text').decode("utf8")
		print(text)
		for word in replace(text).split():
			counter[word] += 1

except KeyboardInterrupt:
	pass

for k,v in counter.items():
	if v == 1:
		print(k)
