#!/usr/bin/env python3
class member:
    def __init__(self, username, password, fname, mname, lname):
        self.username = username
        self.password = password
        self.fname = fname
        self.mname = mname
        self.lname = lname

class admin(member):
    pass

class student(member):
    pass

bruce = admin("admin1", "hahaha", "Bruce","Batman","Padron")
brian = student("student1", "nonono", "Brian", "Robin", "Kim")
print("I have been doing OOP for python incorrectly :/")