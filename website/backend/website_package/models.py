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

sms_text_args = reqparse.RequestParser()
sms_text_args.add_argument('number', type=str, help='No number given')
sms_text_args.add_argument('message', type=str, help='No message given')

# this in conjunction with the "@marshal_with" decorator allows the result of a 
# db search to return a dictionary instead of random stuff within the routes
image_database_parse = {
  'id': fields.String,
  'name': fields.String,
  'url': fields.String,
  'views': fields.Integer
}

class MentModel(db.Model):
  first_name = db.Column(db.String(100), nullable=False)
  last_name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), primary_key = True)
  password = db.Column(db.String(100), nullable=False)
  subject = db.Column(db.String(100), nullable=False)
  level =  db.Column(db.String(100), nullable=False)
  contacts = db.Column(db.String(200), nullable=False)
  auth_token = db.Column(db.Integer, nullable=True)
  #students = db.relationship('StudModel', backref='mentor_email', lazy = True)
  def __repr__(self):
    return f'Mentor(user_name = {name}, first_name = {first_name}, last_name = {last_name}, email = {email}, password = {password}, subject = {subject}, level = {level}, contacts = {contacts}' 
  
ment_post_args = reqparse.RequestParser()
ment_post_args.add_argument('first_name', type=str, help='Mentor did not provide first name')
ment_post_args.add_argument('last_name', type=str, help='Mentor did not provide last name')
ment_post_args.add_argument('email', type=str, help='Email is not provided')
ment_post_args.add_argument('password', type=str, help='Mentor did not provide password')
ment_post_args.add_argument('subject', type=str, help='Mentor did not provide Education category')
ment_post_args.add_argument('level', type=str, help='Mentor must provide level of experience')

mentor_database_parse = {
    'user_name' : fields.String,
    'first_name' :fields.String, 
    'last_name' : fields.String,
    'email' : fields.String,
    'password' : fields.String,
    'subject' : fields.String,
    'level' : fields.String
}


class StudModel(db.Model):
  first_name = db.Column(db.String(100), nullable=False)
  last_name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(100), primary_key=True)
  password = db.Column(db.String(100), nullable=False)
  subject = db.Column(db.String(100), nullable=False)
  level =  db.Column(db.String(100), nullable=False)
  #mentor_id = db.Column(db.Integer, db.ForeignKey('mentor.email'), nullable=True)
  def __repr__(self): 
    return f'Student(user name = {user_name}, first name = {first_name}, last_name = {last_name}, email = {email}, subject = {subject}, level = {level}'

#Used to Parse requests recieved by the routes
stud_post_args = reqparse.RequestParser()
stud_post_args.add_argument('first_name', type=str, help='Student did not provide first name')
stud_post_args.add_argument('last_name', type=str, help='Student did not provide last name')
stud_post_args.add_argument('email', type=str, help='Email is not provided')
stud_post_args.add_argument('password', type=str, help='Student did not provide password')
stud_post_args.add_argument('subject', type=str, help='Student did not pro')
stud_post_args.add_argument('level', type=str, help='Student must provide desired Mentorship level')

student_database_parse = {
    'user_name' : fields.String,
    'first_name' :fields.String, 
    'last_name' : fields.String,
    'email' : fields.String,
    'password' : fields.String,
    'subject' : fields.String,
    'level' : fields.String
}



class SubModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
