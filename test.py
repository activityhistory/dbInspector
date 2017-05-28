# Erin Cole
# dbInspector test file for getting started

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
