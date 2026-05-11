"""
Handles fantasy point calculations and statistical analysis.
"""

import sqlite3
connection_object = sqlite3.connect('FantasyCricketGame.db')
cursor_object = connection_object.cursor()
cursor_object.execute('''CREATE TABLE IF NOT EXISTS Stats(Player TEXT(20),Matches INTEGER,Runs INTEGER,hundreds INTEGER,fifties INTEGER,Value INTEGER,Ctg TEXT(20));''')
query_1 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Kohli',189,8257,28,43,120,'BAT');'''
query_2 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Yuvraj',86,3589,10,21,100,'BAT');'''
query_3 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Rahane',158,5435,11,31,100,'BAT');'''
query_4 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Dhawan',25,565,2,1,85,'AR');'''
query_5 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Dhoni',78,2573,3,19,75,'BAT');'''
query_6 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Axar',67,208,0,0,100,'BWL');'''
query_7 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Pandya',70,77,0,0,75,'BWL');'''
query_8 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Jadeja',16,1,0,0,85,'BWL');'''
query_9 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Kedar',111,675,0,1,90,'BWL');'''
query_10 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Ashwin',136,1914,0,10,100,'AR');'''
query_11 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Umesh',296,9496,10,64,110,'WK');'''
query_12 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Bumrah',73,1365,0,8,60,'WK');'''
query_13 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Bhuwaneshwar',17,289,0,2,75,'AR');'''
query_14 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Rohit',304,8701,14,52,85,'BAT');'''
query_15 = '''INSERT INTO Stats(Player,Matches,Runs,hundreds,fifties,Value,Ctg) VALUES('Kartick',11,111,0,0,75,'AR');'''
cursor_object.execute(query_1)
cursor_object.execute(query_2)
cursor_object.execute(query_3)
cursor_object.execute(query_4)
cursor_object.execute(query_5)
cursor_object.execute(query_6)
cursor_object.execute(query_7)
cursor_object.execute(query_8)
cursor_object.execute(query_9)
cursor_object.execute(query_10)
cursor_object.execute(query_11)
cursor_object.execute(query_12)
cursor_object.execute(query_13)
cursor_object.execute(query_14)
cursor_object.execute(query_15)
connection_object.commit() 
connection_object.close()
















