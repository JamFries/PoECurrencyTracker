# Store public stash tabs using a database
# The database will store the account's public stash tabs
# The database can be referred to when checking for an updated stash
# Code foundation is from https://www.sqlitetutorial.net/sqlite-python/creating-database/
####################################################################
import sqlite3
from sqlite3 import Error

# Create a database connection to an SQLite database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file) # Returns a connection object that represents the database. Allows for various database operations
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

# Create a table from the create_table_sql statement
def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

# Create a new stash tab into the stashTabs table
def create_stashTab(conn, stashTab):

    sql = ''' INSERT INTO stashTabs(id, accountName, stash, stashType, league, items)
    VALUES(?,?,?,?,?,?)
    '''

    cur = conn.cursor()
    cur.execute(sql, stashTab)
    conn.commit()

    return cur.lastrowid

def main():
    database = r"C:\sqlite\db\accountStashTabsPOE.db"

    sql_create_stashTabs_table = ''' CREATE TABLE IF NOT EXISTS stashTabs (
    id TEXT PRIMARY KEY,
    accountName TEXT NOT NULL,
    stash TEXT NOT NULL,
    stashType TEXT NOT NULL,
    league TEXT NOT NULL,
    items TEXT NOT NULL
    );
    '''

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_stashTabs_table)
    else:
        print('Error, cannot create the database connection')

    with conn:
        # Create a new stash tab
        # Use list of stash tabs retrieved from API here

if __name__ == "__main__":
    main()