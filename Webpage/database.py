import sqlite3
conn = sqlite3.connect('./data/beehive.db', check_same_thread=False)
c = conn.cursor()


def findCells(picture):
    cellLocation= []
    c.execute("Select * from Pictures pic where field1 = "+ "'" + picture + "'")
    data= c.fetchall()
    for row in range(len(data)):
        cell= (data[row])
        cellLocation.append(str(cell[5])[44:])
    
    #print( cellLocation)
    return(cellLocation)
