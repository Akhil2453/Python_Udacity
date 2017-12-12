import urllib


def rd_txt():
	quotes = open("/home/akhil/Desktop/Udacity/Python/profanity.txt")
	cof = quotes.read()
	print(cof)
	quotes.close()
	chk_profanity(cof)

def chk_profanity(text_to_check):
	conn = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
	output = conn.read()
	print(output)
	conn.close()


rd_txt()