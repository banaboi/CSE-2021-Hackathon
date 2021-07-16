from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_ngrok import run_with_ngrok

######## FLASK SET-UP STUFF, IF YOU'RE INTERESTED IN WHAT IT ALL DOES GIMME A SHOUT ##########
app = Flask(__name__)
run_with_ngrok(app)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

BACKEND_URL = "http://127.0.0.1:5000"
FRONTEND_URL = "http://127.0.0.1:5500"

CORS(app, origins=FRONTEND_URL, allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)
###########################################################################################


from website_package import routes, models

# This is where Routes are instantiated
api.add_resource(routes.Image, '/image/<string:img_id>')
api.add_resource(routes.Dummy, '/dummy')
api.add_resource(routes.Sms, '/sms')

# This generates a database if one doesn't currently exist
db.create_all()