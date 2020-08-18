#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql

con = pymysql.connect('localhost', 'root', '1111', 'teach')

cur = con.cursor()
cur.execute("SELECT VERSION()")
version = cur.fetchone()
print("Database version: {}".format(version[0]))

cur.execute("SELECT * FROM Docs")

rows = cur.fetchall()

for row in rows:
    print("{0} {1} {2}".format(row[0], row[1], row[2]))
