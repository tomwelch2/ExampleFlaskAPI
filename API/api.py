import pandas as pd
import uuid
from sqlalchemy import create_engine
from flask import Flask, request
from flask_restful import Resource, Api
from time import sleep

sleep(35)


#Connecting to DB and extracting data ---

URL = "mysql+pymysql://root:root@mysql:3306/company"

engine = create_engine(URL)

emp_df = pd.read_sql("SELECT * FROM employees", con = engine).to_dict(orient = "records")



#Creating API and endpoints ---

app = Flask(__name__)

api = Api(app)

class allData(Resource):
    def get(self):
        """Endpoint returns all data from database."""
        return emp_df


api.add_resource(allData, "/all")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
