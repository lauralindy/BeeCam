import sqlite3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             import sqlite3
conn = sqlite3.connect('./data/beehive.db', check_same_thread=False)
c = conn.cursor()

def findCells(picture):
    c.execute("Select * field1 pic where pic.picture = "+ "'" + picture + "'")
    data= c.fetchall()
    print data
