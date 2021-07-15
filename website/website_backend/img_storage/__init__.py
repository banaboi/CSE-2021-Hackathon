from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

BACKEND_URL = "http://127.0.0.1:5000"
FRONTEND_URL = "http://127.0.0.1:5500"

CORS(app, origins=FRONTEND_URL, allow_headers=[
    "Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    supports_credentials=True)


from img_storage import routes, models

api.add_resource(routes.Image, '/image/<string:img_id>')
db.create_all()