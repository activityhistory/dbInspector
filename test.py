# Erin Cole
# dbInspector test file for getting started


# Unit test for showStats function

cnxn = pyodbc.connect(DRIVER, SERVER, DATABASE, UID, PWD)

showStats(cnxn)
