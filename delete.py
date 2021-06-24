import mysql.connector
import users
from tabulate import tabulate 

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'pranita5'
DATABASE = 'music_library_management'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
conn = db.cursor(buffered=True)

def delete():
    try:
        song=input("Enter the name of the song you want to delete\n")
        n=int(input("Select from the following: \n 1. To delete only a particular song\n 2. To delete the song as well as all its assoiciated values\n"))
        if n==1:
            conn.execute(f'DELETE FROM track WHERE track_title="{song}"')
            db.commit()
            print(f"The song {song} has been deleted !")
        elif n==2:
            conn.execute(f'DELETE FROM artist_email WHERE artist_id=(SELECT artist_id FROM track inner join album on track.album_id=album.album_id WHERE track.track_title="{song}")')
            db.commit()
            conn.execute(f'DELETE FROM artist_mobile WHERE artist_id=(SELECT artist_id FROM track inner join album on track.album_id=album.album_id WHERE track.track_title="{song}")')
            db.commit()
            conn.execute(f'DELETE FROM played WHERE track_id=(SELECT track_id FROM track WHERE track_title="{song}")')
            db.commit()
            conn.execute(f'DELETE FROM genre where genre_id=(SELECT genre_id FROM track WHERE track_title="{song}")')
            db.commit()
            conn.execute(f'DELETE FROM album WHERE album_id=(SELECT album_id FROM track WHERE track_title="{song}")')
            db.commit()
            conn.execute(f'DELETE FROM artist WHERE artist_id=(SELECT artist_id FROM track inner join album on track.album_id=album.album_id WHERE track.track_title="{song}")')
            db.commit()
        
            conn.execute(f'DELETE FROM track WHERE track_title="{song}"')
            db.commit()
    except Exception as e:
        print(f"Sorry an error has occured : {e}. Please try again")
        


