"""
Stores detailed statistics and information for individual cricket matches.
"""


import sqlite3
connection_object = sqlite3.connect('FantasyCricketGame.db')
cursor_object = connection_object.cursor()
cursor_object.execute('''CREATE TABLE IF NOT EXISTS Match(Player TEXT(20),Scored INTEGER,Faced INTEGER,Fours INTEGER,Sixes INTEGER,Bowled INTEGER,
Maiden INTEGER,Given INTEGER,Wkts INTEGER,Catches INTEGER,Stumping INTEGER,RunOut INTEGER);''')
connection_object.commit()
query_1 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Pandya',42,36,3,3,30,0,25,0,1,0,0);'''
query_2 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Kohli',102,98,8,2,0,0,0,0,0,0,1);'''
query_3 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Yuvraj',12,20,1,0,48,0,36,1,0,0,0);'''
query_4 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Rahane',49,75,3,0,0,0,0,0,1,0,0);'''
query_5 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Dhawan',32,35,4,0,0,0,0,0,0,0,0);'''
query_6 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Axar',8,4,2,0,48,2,35,1,0,0,0);'''
query_7 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Dhoni',56,45,3,1,0,0,0,0,3,2,0);'''
query_8 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Jadeja',18,10,1,1,60,3,50,2,1,0,1);'''
query_9 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Kedar',65,60,7,0,24,0,24,0,0,0,0);'''
query_10 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Ashwin',23,42,3,0,60,2,45,6,0,0,0);'''
query_11 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Umesh',0,0,0,0,54,0,50,4,1,0,0);'''
query_12 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Bumrah',0,0,0,0,60,2,49,1,0,0,0);'''
query_13 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Bhuwaneshwar',15,12,2,0,60,1,46,2,0,0,0);'''
query_14 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Rohit',46,65,5,1,0,0,0,0,1,0,0);'''
query_15 = '''INSERT INTO Match(Player,Scored,Faced,Fours,Sixes,Bowled,
Maiden,Given,Wkts,Catches,Stumping,RunOut) VALUES('Kartick',29,42,3,0,0,0,0,0,2,0,1);'''
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
