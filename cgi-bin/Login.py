#!/usr/bin/env python3
import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import register_adapter, AsIs
import json
#choice to Login or create new account
#Create new account - hashes pw and puts it in Postgresql
#Sends logged in user to student portal or admin portal
#
#
def create_account(username, fname, mname, lname, password, role):
    #get db connection
    #get credentials
    with open("/var/www/planning/postgre_credentials.json") as file:
        data = json.load(file)
    #get connection to db
    connection = psycopg2.connect(
    database = data["db_name"], 
    user = data["db_user"],
    password = data["db_password"],
    host = data["db_host"],
    port = data["db_port"]
    )
    cur = connection.cursor()
    #check if username is in db
    cur.execute("SELECT net_id FROM Member WHERE net_id LIKE %s", (username,))
    if cur.fetchone() is None:
        connection.rollback()
        cur.execute("""INSERT INTO  member(net_id, first_name, middle_name, last_name, hashed_pass, role)
                                    VALUES (%s, %s, %s, %s, crypt(%s, gen_salt('bf')), %s)""",
                                    (username, fname, mname, lname, password, role))

        connection.commit()
        connection.close()
    else:
        print("account already exists")
        connection.commit()
        connection.close()        

def login(username, password):
    #get db connection
    #get credentials
    with open("/var/www/planning/postgre_credentials.json") as file:
        data = json.load(file)
    #get connection to db
    connection = psycopg2.connect(
    database = data["db_name"], 
    user = data["db_user"],
    password = data["db_password"],
    host = data["db_host"],
    port = data["db_port"]
    )
    cur = connection.cursor()
    #check if username is in db
    cur.execute("SELECT hashed_pass = crypt(%s,'bf') FROM Member WHERE net_id LIKE %s", (password, username,))
    if cur.fetchone() is not None:
        connection.rollback()
        #correct password
        #get role
        cur.execute("SELECT role FROM Member WHERE net_id LIKE %s",(username,))
        user_role = cur.fetchone()[0]
        connection.close()    
        #return html with login
        if user_role.lower() == "student":
            html = """Content-type:text/html\n
                        <html>
                        <head>
                        <title>Student</title>
                        </head>
                        <body>
                        Hello {}
                        </body> 
                        </html>""".format(username)
            return html
        
    else:
        print("incorrect credentials")
        connection.close()     
#create_account("test1", "testerino", "cappuccino", "Al Pacino", "test_password", "student")

login("test1", "test_password")