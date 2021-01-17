import psycopg2
from psycopg2 import OperationalError
from psycopg2.extensions import register_adapter, AsIs
#import numpy as np
#psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
#psycopg2.extensions.register_adapter(np.bool_, psycopg2._psycopg.AsIs)
import csv
import json


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

#open default class file
with open("MyUniversityCourses.csv") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        cur.execute("""INSERT INTO course(course_name, course_name_short,
                                        course_capacity, course_currently_enrolled,
                                        course_instructor, course_section_number, course_location)
                                        VALUES
                                        (%s,%s,%s,%s,%s,%s,%s)""",
                                        (row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
        connection.commit()


connection.close()