from flask import jsonify,make_response, request
from flask_restful import Resource
import datetime
import uuid

from app.api.v1.models.meetup import  meetup_list, meetup_rsvp,MeetUpModels
from app.api.v1.utilis.validations import InputValidation

meetup_model = MeetUpModels()
meetup_validation = InputValidation()

list_data = meetup_list
alert = "Id not found"
empty_alert = "Fields cant be Empty"
class CreateMeetup(Resource):
    """a user should be able to create a meetup"""
    def __init__(self):
        self.model = meetup_model
        self.happeningon = str(datetime.datetime.utcnow())
        self.id = str(uuid.uuid4())
    
    def post(self):
        try:
            data = request.get_json()
            data_state = meetup_validation.check_state(data)

            topic = data['topic']
            location = data['location']
            date = self.happeningon
            public_id = self.id
            tag = data['tag']
            data_id = len(list_data)+1

            if data['topic'] == "":
                return {"message": "%s cant be empty. Input data" %("Topic")},400
            if data['location'] == "":
                return {"message": "Please input location of the meet up"},400
     
            meetupid_validity = meetup_validation.validate_meetup_id(int(data_id))
            if meetupid_validity:
                return {"message: Meetup exist already"},409

            create_meetup = self.model.create_meetup(topic, public_id,data_id, location, date, tag)
            for data in create_meetup:
                response = {
                    "topic": data["topic"],
                    "location": data["location"],
                    "meetup_id": data["meetup_id"],
                    "meetup_date":data["happeningOn"],
                    "id":data["id"]
                }
            return {"status": 201,
                "message": "Meetup successfully created", 
                "user data": response}, 201
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)
class UpcomingMeetup(Resource):
    def get(self):
        """
        a user should be able get details of all upcoming details
        """
        try:
            meetups_upcoming = MeetUpModels().get_meetup()
            return make_response(jsonify({"Upcoming meetup": meetups_upcoming}),200)
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)
class SpecificMeetup(Resource):
    """a should be able to get details of a specific meetup"""
    def __init__(self):
        self.meetup = MeetUpModels()

    def get(self, id):
        """
            a user can get 
            details of a 
            specific meetup
            """
        try:
            verify_id = meetup_validation.validate_meetup_id(int(id))
            if not verify_id:
                return {"message":"Id not found"},404
            specificmeetup= self.meetup.get_specific_meeetup(int(id))
            return make_response(jsonify({"message":specificmeetup}),200)

        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)
class MeetupRsvp(Resource):
    """ a user can RSVPS for a specific meetup """
    def __init__(self):
        self.model = meetup_model
        self.date = str(datetime.datetime.utcnow())
        self.rsvp_id = str(uuid.uuid4())

    def post(self, id):
        try:
            data = request.get_json()
            topic = data['topic']  
            status = data['status']
            username = data['name']
            public_id = self.rsvp_id
            rsvp_date = self.date
            question_id = len(list_data)+1
            
            if data['topic'] == "":
                return {"message": "%s cant be empty. Input data" %("Topic")},400
            if data['status'] == "":
                return {"message": "Please input yes to rsvp and no to reject rsvp"},400
            if data['name'] == "":
                return {"message": "Username can`t be empty. Input data"},400

            verify_id = meetup_validation.validate_meetup_id(int(id))
            if not verify_id:
                return {"message":"Id not found"},404
            if topic == "" or status == ""or username == "":
                return make_response(jsonify({"message":"Fields can`t be empty"}),400)
            user_rsvp = self.model.rsvp_meetup(topic,status,username, public_id, rsvp_date)
            for data in user_rsvp:
                response = {
                    "topic": data["topic"],
                    "rsvp_id": data["rsvp_id"],
                    "meetup_date":data["rsvp_date"],
                    "user": data["user"],
                    "rsvp_date": data["rsvp_date"],
                    "rsvp_status": data["status"],
                }
            return {"status": 201,
                "message": "Meetup successfully created", 
                "user data": response}, 201        
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)
