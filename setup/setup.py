from sqlalchemy import create_engine
from time import sleep

sleep(25)


#Connecting to DB ---

URL = "mysql+pymysql://root:root@mysql:3306/mydb"


engine = create_engine(URL)

con = engine.connect()

#Reading in files with commands ---

statements = []

with open("create_database.sql", "r") as f:
    create_db = f.read().strip()
    statements.append(create_db)

with open("create_table.sql", "r") as f:
    create_table = f.read().strip()
    statements.append(create_table)

with open("insert_data.sql", "r") as f:
    insert_data = f.read().strip()
    statements.append(insert_data)


#Executing queries for setup ---

for query in statements:
    con.execute(query)


con.close()


