from flask_restx import Resource, abort, field, marshal_with
from website_package import db
from website_package.models import StudModel, stu_post_args, student_database_parse
from twilio import Client

class stu_sign_up(Resource):

    #Post request to add new student to datbase
    def post(self, student_id):
        args = stu_post_args.parse_args()
        result = StudModel.query.get(student_id)
        if result:
            abort(409, message="Student is already a member")
        else:
            student = StudModel(user_name = student_id, first_name =args['first_name'], last_name = args['last_name'],
             email = args['email'], password = args['password'], subject = args['subject'], level = args['level'])
            db.session.add(student)
            db.session.commit()


class stu_info(Resource):