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