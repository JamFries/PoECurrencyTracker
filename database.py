# Store public stash tabs using a database
# The database will store the account's public stash tabs
# The database can be referred to when checking for an updated stash
# Code foundation is from https://www.sqlitetutorial.net/sqlite-python/creating-database/
####################################################################
import sqlite3
from sqlite3 import Error

import requests
import json

# Set initial variables used when searching through APIs
league = 'Harvest'
account = 'blurp151'
platform = 'pc'
charName = 'NowCalledAuraStacking'

# Gather a list of all public stash tabs that belong to the player's account
playerStashTabs = []
# Create a list to temporarily store items that are in a single stash tab before being added to the database
stashTabItems = []

# Use pathofexile's stash tab API to find my stash tabs that are listed public
# Start with the change id from poe.ninja
changeID = '776469591-789811728-754081559-852962907-813854915'
stashTabs = requests.get('http://api.pathofexile.com/public-stash-tabs', dict(id=changeID)).json()
nextChangeID = stashTabs['next_change_id']


# Check each stash from the api for the specific account
for entry in stashTabs['stashes']:
    if (entry['accountName'] == account):
        playerStashTabs.append(entry) #Add the stash entry to the list of stash tabs the account has
        for entry2 in entry['items']:
            stashTabItems.append(entry2)

print(playerStashTabs)
print(stashTabItems)
#changeID = nextChangeID

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

    sql = ''' INSERT INTO stashTabs(id, accountName, stash, stashType, league)
    VALUES(?,?,?,?,?)
    '''

    cur = conn.cursor()
    cur.execute(sql, stashTab)
    conn.commit()

    return cur.lastrowid

# Create a new item
def create_item(conn, item):

    sql = ''' INSERT INTO items(id, itemName, typeLine, identified, ilvl, frameType, league, stashTab_id)
    VALUES(?,?,?,?,?,?,?,?)
    '''

    cur = conn.cursor()
    cur.execute(sql, item)
    conn.commit()

    return cur.lastrowid

# Main function
def main():
    # Get player stash tabs


    ################################################
    database = r"C:\sqlite\db\accountStashTabsPOE.db"

    sql_create_stashTabs_table = ''' CREATE TABLE IF NOT EXISTS stashTabs (
    id TEXT PRIMARY KEY,
    accountName TEXT NOT NULL,
    stash TEXT NOT NULL,
    stashType TEXT NOT NULL,
    league TEXT NOT NULL
    );
    '''

    sql_create_items_table = ''' CREATE TABLE IF NOT EXISTS items (
    id TEXT PRIMARY KEY,
    itemName TEXT NOT NULL,
    typeLine TEXT NOT NULL,
    identified INTEGER NOT NULL,
    ilvl INTEGER NOT NULL,
    frameType INTEGER NOT NULL,
    league TEXT NOT NULL,
    stashTab_id INTEGER NOT NULL
    );
    '''

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_stashTabs_table)
        create_table(conn, sql_create_items_table)
    else:
        print('Error, cannot create the database connection')

    with conn:
        # Create a new stash tab
        for tab in playerStashTabs:
            stashTab = (tab['id'], tab['accountName'], tab['stash'], tab['stashType'], tab['league'])
            stashTab_id = create_stashTab(conn, stashTab)

            # Create Items from tab
            for i in stashTabItems:
                item = (i['id'], i['name'], i['typeLine'], i['identified'], i['ilvl'], i['frameType'], i['league'], stashTab_id)
                create_item(conn, item)


if __name__ == "__main__":
    main()