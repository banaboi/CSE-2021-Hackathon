from flask_restx import Resource, abort, fields, marshal_with
from website_package.models import MentModel, ment_post_args ,mentor_database_parse
from website_package import db


class mentor_sign_up(Resource):
    #put request to add a new mentor the database
    @marshal_with(mentor_database_parse)
    def post(self):
        args = ment_post_args.parse_args()
        result = MentModel.query.get(mentor_email)
        if result:
            abort(409, message="Mentor is already a member")
        else:
            mentor = MentModel(first_name = args['first_name'], last_name = args['last_name'], 
            email = args['email'], password = args['password'], subject = args['subject'], level = args['level'])
            db.session.add(mentor)
            db.session.commit()

class mentor_info(Resource):
    
    #Get request to retrieve the students information for a dashboard
    @marshal_with(student_database_parse)
    def get(self, mentor_id):
        result = StudModel.query.get(auth_token)
        if not result:
            abort(404, message ='Invalid User Token')
        return {'fnanme' : str(result.first_name), 'edu_category' : str(result.subject), 'teach_level' : str(result.level), 'student_connections' : str(result.students)}


