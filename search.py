import mysql.connector
import users
from tabulate import tabulate 

HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'pranita5'
DATABASE = 'music_library_management'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
conn = db.cursor(buffered=True)

def search():
    try:
        s_song=input("Enter the name of the song to search\n")
        conn.execute('SELECT track_title FROM track WHERE track_title= %s',(s_song,))
        songname=conn.fetchall()
        db.commit()
        if not songname:
            print('Sorry! the track does not exist in the database')
        else:
            conn.execute(f'select track_title,album_name,artist_name,genre_type,track_lang,play_time,email,mob_num from track inner join album on track.album_id=album.album_id inner join artist on album.artist_id=artist.artist_id inner join genre on track.genre_id=genre.genre_id inner join played on track.track_id=played.track_id inner join artist_email on artist.artist_id=artist_email.artist_id inner join artist_mobile on artist.artist_id=artist_mobile.artist_id where track_title="{s_song}"')
            db.commit()
            query=conn.fetchall()
            print("Track found !")
            print(tabulate(query, headers=['Track Title','Album Name' ,'Artist Name','Genre Type','Track Language','Duration','Artist Email','Artist Mobile'], tablefmt='psql'))
            db.commit()
    except Exception as e:
        print(f"Sorry an error has occured : {e}. Please try again")


    