#!/usr/bin/env python3
import cgi
import psycopg2
import json
import cgitb
import Login
cgitb.enable()

form = cgi.FieldStorage()
net_id = form.getvalue("uname")
upass = form.getvalue("psw")

with open("/var/www/planning/postgre_credentials.json") as file:
    data = json.load(file)

connection = psycopg2.connect(
database = data["db_name"], 
user = data["db_user"],
password = data["db_password"],
host = data["db_host"],
port = data["db_port"])
cur = connection.cursor()

try:
       #login
       print(Login.login(net_id, upass))
       
except Exception as e:
       print("error", e)


finally:
       connection.close()