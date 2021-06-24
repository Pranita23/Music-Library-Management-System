import mysql.connector
from tabulate import tabulate 

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'pranita5'
DATABASE = 'music_library_management'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
conn = db.cursor(buffered=True)

def playlist():
    try:
        playlist=input("Enter name of your playlist \n")
        user_name=input("Enter your name\n")
        n=int(input("Enter the number of songs you want in your playlist\n"))
        print("Songs available in the database:\n")
        conn.execute(f'SELECT track_id,track_title,track_lang FROM track')
        tracklist=conn.fetchall()
        print(tabulate(tracklist, headers=['Track ID', 'Track Name','Track Language'], tablefmt='psql'))
        for i in range(0,n):
            song=input("Enter the name of the track to be added into the playlist\n")
            conn.execute(f'INSERT INTO playlist(user_id,playlist_name,track_name) VALUES((SELECT user_id from users WHERE name="{user_name}"),"{playlist}","{song}")')
            db.commit()
        print(f"\nThe playlist {playlist} contains :\n")
        conn.execute(f'SELECT track_name FROM playlist WHERE playlist_name="{playlist}"')
        yours=conn.fetchall()
        print(tabulate(yours, headers=['Track Name',], tablefmt='psql'))
    except Exception as e:
        print(f"Sorry an error has occured : {e}. Please try again")

