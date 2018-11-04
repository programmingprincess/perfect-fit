import requests
import sys

urlstr = raw_input()
bust = raw_input()

r = requests.get(urlstr)
	letterCol = 0
	numericCol = 0
	bustCol = 0
	lowerNumeric = -1
	upperNumeric = -1
	lowerLetter = ""
	upperLetter = ""

	jsonData = r.json()
	numericSizeCol = 0
	for i in range(3):
		tops = jsonData['data'][i]['title']
		for title in tops:
			#print(item)
			if "Tops" in title:
				#print("Alert")
				sizeTypes = jsonData['data'][i]['headings']
				#print(sizeTypes)
				for j in range(0,len(sizeTypes)):
					if "Bust" in sizeTypes[j]:
						bustCol = j
						continue
					if "Letter" in sizeTypes[j]:
						letterCol = j
						continue
					if "Numeric" in sizeTypes[j]:
						numericCol = j
						continue
				sizeTable = jsonData['data'][i]['table']
				for row in sizeTable:
					if(row[bustCol]==bust):
						size = "Your size: "+row[numericCol]+", which is also an: "+row[letterCol]
						return size
					elif(row[bustCol]<bust):
						lowerNumeric = row[numericCol]
						lowerLetter = row[letterCol]
					elif(row[bustCol]>bust):
						upperNumeric = row[numericCol]
						upperLetter = row[letterCol]
						if(lowerNumeric!=-1):
							size = "Your size is between " + lowerNumeric + "("+lowerLetter+") and "+upperNumeric+"("+upperLetter+")"
							return size
						else:
							return "Pick the smallest size!"
		return "Not Found"