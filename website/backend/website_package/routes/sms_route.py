from flask_restx import Resource
from twilio.rest import Client

class Sms(Resource):
  def post(self):
    # should be set as environment variables, but since python ENV stuff is a nightmare I can't be bothered
    account_sid = "AC20f57cf543afba11d2b113b94d75c5a4"
    auth_token  = "35d33baeacae5cafcbb45bbbdd2dc5b6"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+610429605291", 
        from_="+18582391207",
        body="Yo does this even work")

    print(message.sid)