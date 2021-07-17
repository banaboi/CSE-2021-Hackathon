from flask_restx import Resource, abort, fields, marshal_with
from website_package.models import MentModel, ment_post_args ,mentor_database_parse
from website_package import db


class mentor_sign_up(Resource):
    #put request to add a new mentor the database
    @marshal_with(mentor_database_parse)
    def post(sefl, mentor_id):
        args = ment_post_args.parse_args()
        result = MentModel.query.get(mentor_id)
        if result:
            abort(409, message="Mentor is already a member")
        else:
            mentor = MentModel(user_name = mentor_id, first_name = args['first_name'], last_name = args['last_name'], 
            email = args['email'], password = args['password'], subject = args['subject'], level = args['level'], 'contacts' = args['contacts'])

            db.session.add(mentor)
            db.session.commit()

class mentor_info(Resource):



