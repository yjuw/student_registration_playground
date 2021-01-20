#!/usr/bin/env python3
import cgi

import cgitb
cgitb.enable(display=0, logdir="/test/")

form = cgi.FieldStorage()
if "uname" not in form or "psw" not in form:
    print("<H1>Error</H1>")
    print("Please fill in the name and password fields.")
    
print("<p>name:", form["name"].value)
print("<p>addr:", form["psw"].value)