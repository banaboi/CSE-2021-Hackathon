from flask_restx import Resource, abort, marshal_with
from website_package.models import StudModel, MentModel, signin_post_args


class signIn(Resource):

    #Get request to log a student or mentor into the site
    @marshal_with
    def post(self):
        args = signin_post_args.parse_args()
        isMentor = MentModel.query.get(args['email'])
        isStudent = StudModel.query.get(args['email'])
        if isMentor:
            if (isMentor.password == args['password']):
                #return auth token with user_id and user_type
                return { "mentor_id" : isMentor.user_id, "user_type" : 'Mentor'}, 200 
            else:
                abort(404, message='Incorrect password') 

        elif isStudent:

            if (isStudent.password == args['password']):
                #return authentication token 
                return { "student_id" : isStudent.user_id, "user_type" : 'Mentor'}, 200
            else:
                abort(404, message="Incorrect password")

        else: 
            abort(409, message = "Invalid Email address")