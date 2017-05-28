# Erin Cole
# Filename: showStats
# Description: This file shows initial statistical information about a database.#               It is meant to be run after establishing a connection to a SQL
#               database



# Function Name: showStats()
# Parameters: cnxn, a connection to a database server
# Descsroption: this function returns a formmated display of the initial 
#               information typically queried from a database after a connection#               has been established.
# Return Value: a formatted string of the initial statistics of a database

def showStats(cnxn):
    cursor = cnxn.cursor()
    cursor.execute("""
                    select * from public.users
                    """)
    rows = cursor.fetchall()

    return rows 
