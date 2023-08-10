from twilio.rest import Client

account_sid = "AC702100012af1958b58233843fcf3d08f"
auth_token = "abcbe0962fd90eff6cb617dfbd0a2641"

client = Client(account_sid, auth_token)

call = client.messages.create(
    to="+919728288398",
    from_="+13254139292",
    body="hello arjun kaise ho?"
)
