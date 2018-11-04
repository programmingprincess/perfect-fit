import requests
import sys
urlstr = raw_input()
size = raw_input()
r = requests.get(urlstr)
searchString = "Letter"
bustCol = 0
sizeCol = 0
if size.isdigit():
	searchString = "Numeric"

jsonData = r.json()
numericSizeCol = 0
for i in range(3):
	tops = jsonData['data'][i]['title']
	for title in tops:
		#print(item)
		if "Tops" in title:
			#print("Alert")
			sizeTypes = jsonData['data'][i]['headings']
			for j in range(0,len(sizeTypes)):
				if "Bust" in sizeTypes[j]:
					bustCol = j
					continue
				if searchString in sizeTypes[j]:
					#print(sizeTypes[j], j)
					sizeCol = j
					continue
			sizeTable = jsonData['data'][i]['table']
			for row in sizeTable:
				if(row[sizeCol] == size):
					return row[bustCol]