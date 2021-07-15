from img_storage import db, api
from img_storage.models import ImgModel, img_post_args, img_put_args
from flask_restful import Api, Resource, abort, fields, marshal_with

resource_fields = {
  'id': fields.String,
  'name': fields.String,
  'url': fields.String,
  'views': fields.Integer
}

class Image(Resource):
  @marshal_with(resource_fields)
  def get(self, img_id):
    result = ImgModel.query.filter_by(id=img_id).first()
    if not result:
      abort(404, message="Image not found")
    return result
  
  def post(self, img_id):
    print(1)
    args = img_post_args.parse_args()
    # result = ImgModel.query.filter_by(id=img_id).first()
    # print(2)
    # if result:
    #   abort(409, message="Image already exists")
    image = ImgModel(id=img_id, name=args['name'], url=args['url'], views=args['views'])
    print(3)
    db.session.add(image)
    print(4)
    db.session.commit()
    print(5)
    return {}, 200

  @marshal_with(resource_fields)
  def put(self, img_id):
    args = img_put_args.parse_args()
    result = ImgModel.query.filter_by(id=img_id).first()
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
    
  def delete(self, img_id):
    # del images[img_id]
    return {}, 204