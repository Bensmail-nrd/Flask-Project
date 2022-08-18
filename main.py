# import all neccessary  
from flask import Flask, render_template
from flask_restful import Api,Resource

# launch the Flask app
app = Flask(__name__)

# launch the Api handler for the app
api = Api(app)

# Create a class that inherits from Resouce, just to handle and custamize the request type
class Hello(Resource):
    # override the get methode to handle its parameters
    def get(self,name):
        return {"data":"this is a response from your get request for you " + name}

# add the resouce class to the api, then set a route for it
api.add_resource(Hello,"/hellorequest/<string:name>")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
