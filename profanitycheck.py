def rd_txt():
	quotes = open("/home/akhil/Desktop/Udacity/Python/profanity.txt")
	cof = quotes.read()
	print(cof)
	quotes.close()

rd_txt()