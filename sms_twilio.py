#from twilio.rest import TwilioRestClient
#from twilio import rest

# Your Account sid and Auth token from twilio.com/user/account

#account_sid = "ACc165f64757b95fa2ba936fdd4cc01df0"
#auth_token = "e7393d8c9319cb9468eb8e38454b7c1b"

#client = rest.TwilioRestClient(account_sid, auth_token)

#message = client.sms.messages.create(
#	body = "Nishita?! I Love you <3",
#	to = "+918655752503S",
#	from_="+16153921256 ")
#print message.sid


import twilio

client = twilio.rest.TwilioRestClient()