#!/usr/bin/env python3
import cgi

import cgitb
cgitb.enable(display=0, logdir="/test/")

form = cgi.FieldStorage()
first_name = form.getvalue("uname")
password = form.getvalue("psw")

print("Content-type:text/html")
print("")
print("")
print("Hello")
print("")
print("")
print("")
print(" Hello", first_name)
print("")
print("")