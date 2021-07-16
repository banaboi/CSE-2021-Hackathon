from website_package import db, api
from website_package.models import ImgModel, img_post_args, img_put_args
from flask_restx import Api, Resource, abort, fields, marshal_with
from os import system

# this in conjunction with the "@marsha_with" decorator allows the result of a 
# db search to return a dictionary instead of random stuff
resource_fields = {
  'id': fields.String,
  'name': fields.String,
  'url': fields.String,
  'views': fields.Integer
}

# SITE/image ROUTE
class Image(Resource):
  # GET request route
  @marshal_with(resource_fields)
  def get(self, img_id):
    result = ImgModel.query.get(img_id)
    if not result:
      abort(404, message="Image not found")
    return result
  
  # POST request route
  def post(self, img_id):
    args = img_post_args.parse_args()
    result = ImgModel.query.get(img_id)
    if result:
      abort(409, message="Image already exists")
    image = ImgModel(id=img_id, name=args['name'], url=args['url'], views=args['views'])
    db.session.add(image)
    db.session.commit()
    return {}, 200

  # PUT request route, edits an image's fields
  @marshal_with(resource_fields)
  def put(self, img_id):
    args = img_put_args.parse_args()
    result = ImgModel.query.get(img_id)
    if not result:
      abort(409, message="Image doesn't exist")
    if args['name']:
      result.name = args['name']
    if args['url']:
      result.url = args['url']
    if args['views']:
      result.views = args['views']

    db.session.commit()
    return result

  # DELETE request route (very bad and doesn't work)  
  def delete(self, img_id):
    # this is very bad, big nono, don't leave this in for production
    system("rm ./database.db")
    return {}, 204

# SITE/dummy ROUTE
class Dummy(Resource):
  def get(self):
    return {"text": "Hey you're a pretty cool dude"}