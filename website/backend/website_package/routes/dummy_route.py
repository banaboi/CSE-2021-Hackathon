from flask_restx import Resource

class Dummy(Resource):
  def get(self):
    return {"text": "Hey you're a pretty cool dude"}