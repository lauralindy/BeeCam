import sqlite3
conn = sqlite3.connect('./data/example.db', check_same_thread=False)
c = conn.cursor()

"""
Initializes tables
Params:
    None
"""
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS users (first_name text, last_name text, email text, phoneNumber text, password text, profileType text)''')
    #c.execute('''CREATE TABLE IF NOT EXISTS survey (q1 text, q2 text, q3 text)''')

"""
Adds a user to the users database
Params:
    first_name, last_name, email, password, profileType
"""
def create_user(first_name, last_name, email, phoneNumber, password,profileType):
    if user_exists(email):
        return False
    else:
        sql = "INSERT INTO users VALUES(?, ?, ?, ?,?,?)"
        c.execute(sql, (first_name, last_name, email, phoneNumber, password, profileType))
        conn.commit()
        return True

"""
Checks if user's email is already registered within the database
"""
def user_exists(email):
    c.execute("Select * from users u where u.email = "+ "'" + email + "'")
    data=c.fetchall()

    if len(data) == 0:
        return False
    else:
        return True
"""
Updates user profileType
"""
def user_update(email, profileType):
    c.execute("UPDATE users SET profileType='" + profileType + "' WHERE profileType = '0' AND email='" + email + "'")
    conn.commit()

"""
Checks if login information is correct
"""
def user_authentication(email, password):
    c.execute("Select * from users u where u.email = "+ "'" + email + "' AND u.password= "+"'" + password + "'")
    data=c.fetchall()

    if len(data)==0:
        return False
    else:
        return True

"""
Params:
    None
"""
def print_users():
    for row in c.execute("Select * from users"):
        print row

if __name__ == "__main__":
    # Creating Tables
    create_table()

    # Testing create_user
    print_users()
