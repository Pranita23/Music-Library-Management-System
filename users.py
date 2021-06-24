import mysql.connector
import pandas as pd
import time as t


USERNAME = 'root'
HOSTNAME = 'localhost'
PASS = 'pranita5'
DATABASE = 'music_library_management'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASS, db=DATABASE)
conn = db.cursor(buffered=True)


def adding():
    y=input("Enter your name \n")
    conn.execute("USE music_library_management")
    conn.execute(f'INSERT INTO users(name) values ("{y}")')
    db.commit()

def login():
    
    try:
        db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASS, db=DATABASE)
        conn = db.cursor(buffered=True)
        print('Enter username: ')
        username = input()
        conn.execute('SELECT name FROM users WHERE name= %s',(username,))
        username1=conn.fetchall()
        db.commit()
        if not username1:
            print('Username does not exist in the database\n')
            adding()
            print("User added to database !\n")
        else:
            print('Logged In!\n')
        db.commit()
    except Exception as e:
        print(f"Sorry an error has occured : {e}. Please try again")

login()
