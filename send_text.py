from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC4404ff620648cca845d7bbfff463263c"
auth_token  = "23e028cf2ed319587691d11d7bd39481"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Testing twilio",
    to="+353831533083",    # Replace with your phone number
    from_="+441158243169") # Replace with your Twilio number
print message.sid