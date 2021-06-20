from twilio.rest import Client  
sid = "AC6c6a6f488f2a60ec3f98aa0d592ba6fc"
auth_token = "c46caf726161fa4ce7c0ee3aaa2f3214"

client =Client(sid,auth_token)
resp = client.messages.create(body="asdfghjkl;",from_="+17036599445",to="+919315171849")

print(resp.sid)