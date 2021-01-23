#!/usr/bin/env python3
import cgi
import psycopg2
import json
import cgitb
import bcrypt
cgitb.enable(display=0, logdir="/test/")

form = cgi.FieldStorage()
net_id = form.getvalue("uname")
upass = form.getvalue("psw")

with open("/var/www/planning/postgre_credentials.json") as file:
    data = json.load(file)
with open("/var/www/planning/salt.txt", "r") as file:
      salt = file.read()

connection = psycopg2.connect(
database = data["db_name"], 
user = data["db_user"],
password = data["db_password"],
host = data["db_host"],
port = data["db_port"])
cur = connection.cursor()

upass_salted = bcrypt.scrypt(bytes(upass, encoding='utf8'), bytes(salt, encoding='utf8'))

try:
       # member = cur.execute("""SELECT net_id
       #                      FROM member
       #                      WHERE net_id = %s
       #                      AND hashed_pass = %s""",
       #                      (net_id, upass_salted))
       print ("Content-type:text/html\n") 
       print ("<html>") 
       print ("<head>") 
       print ("<title>First CGI Program</title>") 
       print ("</head>") 
       print ("<body>") 
       print("testerino")
       print ("</body>") 
       print ("</html>")
except:
       print("error")


finally:
       connection.close()