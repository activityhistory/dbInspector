# Erin Cole
# dbInspector test file for getting started

#TODO figure which initial stats to include in query
#     look through visualization book
#     start planning layout of visualization


import pyodbc
import showStats
# Unit test for showStats function

# Initialize needed variables
driver = '{PostgreSQL ODBC DRIVER(UNICODE)}'
server = 'localhost'
database = 'postgres'
uid = 'postgres'
pwd = ' ' # password intentionally not written for security

# Start of first test
# This unit test selects all rows from a table called 'users'
cnxn = pyodbc.connect(DRIVER = driver, SERVER = server, DATABASE = database, UID = uid, PWD = pwd)

rows = showStats.showStats(cnxn)

for row in rows
        print (row)

cnxn.close()
