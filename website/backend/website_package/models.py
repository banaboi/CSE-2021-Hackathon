from website_package import db
from flask_restx import Api, Resource, reqparse, abort, fields, marshal_with

# Tells the database what model to use for the Image Model table (i.e. what columns it has and what values those columns should contain)
class ImgModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  url = db.Column(db.String(100), nullable=False)
  views = db.Column(db.Integer, nullable=False)

  def __repr__(self):
    return f'Image(name = {name}, url = {url}, views = {views})'

# Used in routes.py, parses requests recieved by the routes 
img_post_args = reqparse.RequestParser()
img_post_args.add_argument('name', type=str, help='No name of image given', required=True)
img_post_args.add_argument('url', type=str, help='No url of image given', required=True)
img_post_args.add_argument('views', type=int, help='No views of image given', required=True)

img_put_args = reqparse.RequestParser()
img_put_args.add_argument('name', type=str, help='No name of image given')
img_put_args.add_argument('url', type=str, help='No url of image given')
img_put_args.add_argument('views', type=int, help='No views of image given')


# this in conjunction with the "@marsha_with" decorator allows the result of a 
# db search to return a dictionary instead of random stuff within the routes
resource_fields = {
  'id': fields.String,
  'name': fields.String,
  'url': fields.String,
  'views': fields.Integer
}