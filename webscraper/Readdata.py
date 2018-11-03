import requests

def get_Bust(size):
	r = requests.get('https://heabuh.com/perfectfit/getchartforstore?store_name=guess')
	searchString = "Letter"
	bustCol = 0
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

def get_Size(bust):
	r = requests.get('https://heabuh.com/perfectfit/getchartforstore?store_name=gucci')
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
						if(lowernumeric!=-1):
							size = "Your size is between " + lowernumeric + "("+lowerLetter+") and"+upperNumeric+"("+upperLetter+")"
							return size
						else
							return "Pick the smallest size!"
		return "Not Found"


def main():
	
	size = raw_input("What is your size? ")
	bust = get_Bust(size)
	print("Bust Size: ", bust)
	yourBust = raw_input("What is your bust? ")
	convertedSize = get_Size(yourBust)
	print(convertedSize)


	
if __name__ == '__main__':
    main()