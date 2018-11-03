import requests

def get_Bust(urlstr, size):
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

def get_Size(urlstr, bust):
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
def cut_url(urlstr):
	first_index = urlstr.find('http://')
	if first_index!=-1:
		first_index+=7
		urlstr = urlstr[first_index:]
	first_index = urlstr.find('https://')
	if first_index!=-1:
		first_index+=8
		urlstr = urlstr[first_index:]
	first_index = urlstr.find('www.')
	if first_index!=-1:
		first_index+=4
		urlstr = urlstr[first_index:]
	lastIndex = urlstr.rfind('.')
	if(lastIndex!=-1):
		urlstr = urlstr[0:lastIndex]
	return urlstr

def main():
	website = raw_input("Enter website ")
	website= cut_url(website)
	urlstr = 'https://heabuh.com/perfectfit/getchartforstore?store_name='+website
	size = raw_input("What is your size in "+ website+ "?")
	bust = get_Bust(urlstr,size)
	decoded_value = bust.encode('utf-8')
	print(type(decoded_value))
	print(decoded_value[0:len(decoded_value)-2])
	website = raw_input("Enter website ")
	website = cut_url(website)
	urlstr = 'https://heabuh.com/perfectfit/getchartforstore?store_name='+website
	convertedSize = get_Size(urlstr,bust)
	print(convertedSize)



	
if __name__ == '__main__':
    main()