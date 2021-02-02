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
    pass

create_account("test1", "testerino", "cappuccino", "Al Pacino", "test_password", "student")

