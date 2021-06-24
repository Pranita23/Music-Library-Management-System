import mysql.connector
import users
from tabulate import tabulate 

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'pranita5'
DATABASE = 'music_library_management'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
conn = db.cursor(buffered=True)

def display():
    try:
        db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
        conn = db.cursor(buffered=True)
        choice=int(input("Make a choice :\n 1.Display all the tracks\n 2.Display all the albums\n 3.Display all the artists\n"))
        if choice == 1:
            conn.execute(f'SELECT track_id, track_title,album_name,artist_name FROM track inner join album on track.album_id=album.album_id inner join artist on artist.artist_id=album.artist_id')
            db.commit()
            tracks=conn.fetchall()
            db.commit()

            print(tabulate(tracks, headers=['Track ID', 'Track Title', 'Album Name', 'Artist Name'], tablefmt='psql'))

        elif choice==2:
            conn.execute(f'SELECT album_id,album_name,artist_name FROM album inner join artist on album.album_id=artist.artist_id')
            db.commit()
            albums=conn.fetchall()
            db.commit()
            print(tabulate(albums, headers=['Album ID', 'Album Name', 'Artist Name'], tablefmt='psql'))
    
        elif choice==3:
            conn.execute(f'SELECT artist_id, artist_name FROM artist')
            db.commit()
            artists=conn.fetchall()
            db.commit()
            print(tabulate(artists, headers=['Artist ID', 'Artist Name'], tablefmt='psql'))
        else:
            print("Please enter a valid choice")
    except Exception as e:
        print(f"Sorry an error has occured : {e}. Please try again")

