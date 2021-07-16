from flask_restx import Resource
from twilio.rest import Client
from website_package.models import sms_text_args

class Sms(Resource):
  def post(self):
    args = sms_text_args.parse_args()
    # should be set as environment variables, but since python ENV stuff is a nightmare and I can't be bothered
    account_sid = "AC20f57cf543afba11d2b113b94d75c5a4"
    # sometimes you need to grab a new one from the website
    auth_token  = "930bd3b50be71cdaea20fef820fafcbf"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=args['number'], 
        from_="+18582391207",
        body=args['message'])