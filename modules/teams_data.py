"""
Manages fantasy team creation, storage, and retrieval.
"""

import sqlite3
connection_object = sqlite3.connect('FantasyCricketGame.db')
cursor_object = connection_object.cursor()
cursor_object.execute('''CREATE TABLE IF NOT EXISTS Teams(Name Text(20),Players Text(1000),Value INTEGER);''')
connection_object.commit()
connection_object.close()
