import mysql.connector
import users
from tabulate import tabulate 

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'pranita5'
DATABASE = 'music_library_management'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
conn = db.cursor(buffered=True)

def update():
    
    try:
        n=int(input("Please enter:\n 1.To change the name of a song\n 2.To change the name of an album\n 3.To change the name of an artist\n 4.To change the genre\n 5.To change the duration of the song\n "))
        if n==1:
            track=input("Enter the name of the song you want to modify\n")
            new_title=input("Enter the new track name\n")
            conn.execute(f'UPDATE track SET track_title="{new_title}" WHERE track_title="{track}"')
            db.commit()
            print(f"{track} was succesfully changed to {new_title}")
        elif n==2:
            album=input("Enter the name of the album you want to change\n")
            new_album=input("Enter the new album name\n")
            conn.execute(f'UPDATE album SET album_name="{new_album}" WHERE album_name="{album}"')
            db.commit()
            print(f"{album} was succesfully changed to {new_album}")
        elif n==3:
            artist=input("Enter the name of the artist you want to change\n")
            new_artist=input("Enter the new artist\n")
            conn.execute(f'UPDATE artist SET artist_name="{new_artist}" WHERE artist_name="{artist}"')
            db.commit()
            print(f"{artist} was succesfully changed to {new_artist}")
        elif n==4:
            genre=input("Enter the name of the genre you want to change\n")
            new_genre=input("Enter the new genre\n")
            conn.execute(f'UPDATE genre SET genre_type="{new_genre}" WHERE genre_type="{genre}"')
            db.commit()
            print(f"{genre} was succesfully changed to {new_genre}")
        elif n==5:#doesnt work lols
            dur=input("Enter the song for which duration has to be changed\n")
            new_dur=float(input("Enter the new duration\n"))
            conn.execute(f'UPDATE played SET play_time={new_dur} WHERE track_id=(select played.track_id from(select played.track_id from track inner join played on track.track_id=played.track_id where track.track_title="{dur}")as t)')
            db.commit()
            print(f"{dur} was succesfully changed to {new_dur}")
        else:
            print("Please enter a valid input\n")
    except Exception as e:
        print(f"Sorry an error has occured : {e}. Please try again")
