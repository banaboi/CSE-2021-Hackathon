from flask_restx import Resource, abort, marshall_with
from website.packages.models import StudModel, MentModel, stud_post_args, ment_post_args, mentor_database_parse, stud_database_parse
from website_package import db


class signIn(Resource):

    #Get request to log a student or mentor into the site
    @marshall_with
    def get(self, email, password):
        isMentor = MentModel.query.get(email)
        isStudent = StudModel.query.get(email)
        if isMentor:
            if (isMentor.password == password):
                #return auth token with user_id and user_type
                return { "mentor_id" : isMentor.user_id, "user_type" : 'Mentor'}, 200 
            else:
                abort(404, message='Incorrect password') 

        elif isStudent:

            if (isStudent.password == password):
                #return authentication token 
                return { "student_id" : isStudent.user_id, "user_type" : 'Mentor'}, 200
            else:
                abort(404, message="Incorrect password")

        else: 
            abort(409, message = "Invalid Email address")