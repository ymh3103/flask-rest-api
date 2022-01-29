from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#Inisiasi Object Flask

app = Flask(__name__)

#Inisiasi Object flask_restful

api = Api(app)

#Inisiasi Object flask_cors

CORS(app)

#Inisiasi Variabel Kosong Bertipe Dictionary (Dictionary = JSON) Variabel Global
friends = {}

#Membuat class Resource
class Resources(Resource):
    # metode get dan post
    def get(self):
        return friends
    
    def post(self):
        name = request.form["name"]
        email = request.form["email"]
        address = request.form["address"]
        friends["name"] = name
        friends["email"] = email
        friends["address"] = address
        response = {"messages" : "api using flask"}
        return response

#Set Up Resource
api.add_resource(Resources, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)