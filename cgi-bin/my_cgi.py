#!/usr/bin/env python3
import cgi
import psycopg2
import json
import cgitb
import bcrypt
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

net_id = "admin1"
upass = b"BuenosDias"
test_salt = b'$2b$12$gCQYAmpaK0sKum4wrt/j4.'
try:
       member = cur.execute("""SELECT hashed_pass
                            FROM member
                            WHERE net_id = %s""",
                            (net_id,))
       
       upass = bcrypt.hashpw(upass, test_salt)
       member_pass = bytes(cur.fetchone()[0].encode("utf-8"))
       is_member = upass == member_pass
       
       print("Content-type:text/html\n")
       print("<html>") 
       print("<head>") 
       print("<title>Who are you?</title>") 
       print("</head>") 
       print("<body>") 
       print("hi", is_member)
       print("</body>") 
       print("</html>")
except Exception as e:
       print("error", e)


finally:
       connection.close()