import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import register_adapter, AsIs
import json
import bcrypt



#get credentials
with open("postgre_credentials.json") as file:
    data = json.load(file)

def reset_connection():
    if 'connection' not in locals():
        connection = psycopg2.connect(
        database = data["db_name"], 
        user = data["db_user"],
        password = data["db_password"],
        host = data["db_host"],
        port = data["db_port"]
        )
        cur = connection.cursor()
        return connection,cur;
    else:
        connection.close()
        connection = psycopg2.connect(
        database = data["db_name"], 
        user = data["db_user"],
        password = data["db_password"],
        host = data["db_host"],
        port = data["db_port"]
        )
        cur = connection.cursor()
        return connection, cur;

connection, cur = reset_connection()
connection.set_client_encoding('UTF8')
password = b'BuenosDias'
salt = b'$2b$12$gCQYAmpaK0sKum4wrt/j4.'
hashed = bcrypt.hashpw(password, salt)

#delete_name = "admin1"
#cur.execute("""DELETE FROM member WHERE net_id = 'admin1'""")
#connection.commit()
print(hashed)
cur.execute("""INSERT INTO  member(net_id, first_name, last_name, hashed_pass, role)
                            VALUES (%s, %s, %s, %s, %s)""",
                            ("admin1", "Bruce", "Wayne", hashed, "Admin"))

connection.commit()

connection.close()