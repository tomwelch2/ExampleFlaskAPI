import json
import pandas as pd
import jwt
import uuid
from sqlalchemy import create_engine
from flask import Flask, request
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from time import sleep
from functools import wraps

sleep(35)


#Connecting to DB and extracting data ---

URL = "mysql+pymysql://root:root@mysql:3306/company"

engine = create_engine(URL)

emp_df = pd.read_sql("SELECT * FROM employees", con = engine).to_dict(orient = "records")

users_df = pd.read_sql("SELECT * FROM users", con = engine).to_dict(orient = "records")
usernames = [user["username"] for user in users_df]
passwords = [user["password"] for user in users_df]

#Creating API and endpoints ---

app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app)
app.config["SECRET_KEY"] = str(uuid.uuid4())

@auth.verify_password
def verify_password(username, password):
    if not (username and password):
        return False
    
    if username in usernames and password in passwords:
        return True



class Login(Resource):
    @auth.login_required
    def get(self):
        global token
        token = jwt.encode({
            "user": request.authorization.username
        }, app.config["SECRET_KEY"])

        return json.dumps({"Token": token.decode("UTF-8")})


def verify_token(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        received_token = request.args.get("token", None)

        if not received_token or received_token != token.decode("UTF-8"):
            return {"Error": "Invalid or missing API key"}
        
        return f(*args, **kwargs)
    
    return decorator
        

class allData(Resource):
    @verify_token
    def get(self):
        """Endpoint returns all data from database."""
        return emp_df

class filterData(Resource):
    @verify_token
    def get(self, empid):
        return [emp for emp in emp_df if emp["emp_id"] == empid][0]


api.add_resource(allData, "/all")
api.add_resource(Login, '/login')
api.add_resource(filterData, '<int:empid>')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 4000)
