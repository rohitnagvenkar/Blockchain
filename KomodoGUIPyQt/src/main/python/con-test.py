#!/usr/bin/python

import MySQLdb

dbconnect = MySQLdb.connect("3.16.180.203", "myname", "mypassword", "komodoGUI")

cursor = dbconnect.cursor()  
cursor.execute("SELECT VERSION()")

data = cursor.fetchone()  
if data:  
    print('Version retrieved: ', data)
else:  
    print('Version not retrieved.')

dbconnect.close()