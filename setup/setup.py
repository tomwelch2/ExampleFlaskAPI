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

with open('create_users_tbl.sql', "r") as f:
    create_users_tbl = f.read().strip()
    statements.append(create_users_tbl)

with open("add_admin_user.sql", "r") as f:
    add_admin_user = f.read().strip()
    statements.append(add_admin_user)

#Executing queries for setup ---

for query in statements:
    con.execute(query)


con.close()


