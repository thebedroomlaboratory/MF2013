#!/usr/bin/python

# This script is used for all the heavy lifting in the
# connections with the database

import MySQLdb

# Database specific settings
HOST="localhost"
USER="root"
PASS="password"
DB="tbl_mf2013"

cur = None
conn = None

# Database insert statements
INSERT = 'INSERT INTO {0} ({1}) VALUES ({2})'
cols={'oven' : 'temp, status'
      , 'temp' : 'override, lux, temp, status'
      , 'people' : 'counter, switch'}

def getInsert(id):
	str='%s'
	delm=","
	columns=cols[id].split(delm)
	app=[]

	for x in range(0, len(columns)):
		app.append(str)
	
	return INSERT.format(id, cols[id], delm.join(app)) 

def connect():
	global cur
	global conn

    	conn = MySQLdb.connect(host=HOST,
                     user=USER,
                      passwd=PASS,
                      db=DB)
	cur = conn.cursor()
	return

def disConnect():
	global cur
	global conn

    	conn.close()
	return

def insertRow(tbl, values):
	global cur
	global conn

    	try:
		cur.execute(getInsert(tbl),
			    values)
		conn.commit()
    	except MySQLdb.Error, e:
            	conn.rollback()
    	return
