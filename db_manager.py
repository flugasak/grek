"""
File: db_manager.py
Author: FlyOnTheWall

Description:
    Handles the database for grek.py

Usage:
    <Provide instructions on how to use the code in this file, if applicable.>

Dependencies:
    <List any external libraries or modules required by this file.>

Notes:
    <Add any additional notes or information that might be useful for other developers.>
"""

import sqlite3
from os.path import getsize

class grekData:
    def __init__(self, db_file):
        # Create a connection and a cursor
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.dbsize = getsize(db_file)
        self.check_database()

    def check_database(self):
        # Check for options
        self.cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table'")
        result = self.cursor.fetchone()[0]
        if result == 0:
            # The database is empty
            print("database empty.. populating")
            self.populate()
        elif result != 4:
            # Something's wrong, let's run the repopulation
            print("database empty.. populating")
            self.populate()
        else:
            print(f"Database loaded. ({self.dbsize} bytes)")

    def populate(self):
        # Create a table of configuration values
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS config (id INTEGER PRIMARY KEY AUTOINCREMENT, option TEXT, value TEXT)''')
        # Create a table of panels
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS panels (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            name TEXT NOT NULL, 
                            baseURI TEXT NOT NULL,
                            bearer TEXT)
                            ''')
        # Create a table with servers
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS servers (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            panel INTEGER NOT NULL,
                            game TEXT NOT NULL, 
                            name TEXT NOT NULL, 
                            description TEXT)''')
        # Create with applications
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS applications (
                            id INTEGER PRIMARY KEY AUTOINCREMENT, 
                            server INTEGER NOT NULL, 
                            discord_name TEXT NOT NULL, 
                            mojang_name TEXT NOT NULL)'''
                            )
        # Commit changes
        self.conn.commit()
        print('Database repopulated')

    # List all stored panels
    def list_panels(self):
        sql="SELECT * FROM panels"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # Add a panel to the list    
    def add_panel(self, args):
        name=args[1]
        baseURI=args[2]
        bearer=args[3]
        sql="INSERT INTO panels (name, baseURI, bearer) VALUES (?,?,?)"
        self.cursor.execute(sql, (name,baseURI,bearer))
        self.conn.commit()

    # Remove a panel from the list
    def del_panel(self, args):
        id=args[1]
        sql="DELETE FROM panels WHERE id = (?)"
        self.cursor.execute(sql,(id))
        self.conn.commit()
        
    # List all stored servers
    def list_servers(self):
        sql="SELECT * FROM servers"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # Add a server to the list    
    def add_server(self, args):
        game="Minecraft"
        name=args[1]
        description=args[2]
        sql="INSERT INTO servers (game, name, description) VALUES (?,?,?)"
        self.cursor.execute(sql, (game,name,description))
        self.conn.commit()

    # Remove a server from the list
    def del_server(self, args):
        id=args[1]
        sql="DELETE FROM servers WHERE id = (?)"
        self.cursor.execute(sql,(id))
        self.conn.commit()

