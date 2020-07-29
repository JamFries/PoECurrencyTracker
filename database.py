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
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_connection(r"C:\sqlite\db\accountStashTabsPOE.db")