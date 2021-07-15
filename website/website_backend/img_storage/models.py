from img_storage import db
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

class ImgModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  url = db.Column(db.String(100), nullable=False)
  views = db.Column(db.Integer, nullable=False)

  def __repr__(self):
    return f'Image(name = {name}, url = {url}, views = {views})'

img_post_args = reqparse.RequestParser()
img_post_args.add_argument('name', type=str, help='No name of image given', required=True)
img_post_args.add_argument('url', type=str, help='No url of image given', required=True)
img_post_args.add_argument('views', type=int, help='No views of image given', required=True)

img_put_args = reqparse.RequestParser()
img_put_args.add_argument('name', type=str, help='No name of image given')
img_put_args.add_argument('url', type=str, help='No url of image given')
img_put_args.add_argument('views', type=int, help='No views of image given')