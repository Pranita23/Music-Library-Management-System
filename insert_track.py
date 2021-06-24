import mysql.connector
import users


HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'pranita5'
DATABASE = 'music_library_management'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
conn = db.cursor(buffered=True)

def insert():
    try:
        print("Please enter the following details in order to insert a track")
        tracktitle=input("enter the name of the track\n")
        tracklanguage=input("enter the language of the song\n")
        genre=input("enter the genre\n")
        albumname=input("enter the name of the album\n")
        artistname=input("enter name of the artist\n")
        artistemail=input("enter email of the artist\n")
        artistmobile=input("enter mobile number of artist\n")
        duration= float(input("enter duration of song\n"))
        conn.execute(f'INSERT INTO genre(genre_type) VALUES ("{genre}")')
        conn.execute(f'INSERT INTO artist(artist_name) VALUES("{artistname}")') 
        conn.execute(f'INSERT INTO album(album_name,artist_id) VALUES("{albumname}",(SELECT artist_id FROM artist  WHERE artist_name="{artistname}"))')
        conn.execute(f'INSERT INTO artist_email(artist_id,email) VALUES((SELECT artist_id FROM artist WHERE artist_name="{artistname}"),"{artistemail}")')
        conn.execute(f'INSERT INTO artist_mobile(artist_id,mob_num) VALUES((SELECT artist_id FROM artist WHERE artist_name="{artistname}"),"{artistmobile}")')
        conn.execute(f'INSERT INTO track(track_title,track_lang,album_id,genre_id) VALUES ("{tracktitle}","{tracklanguage}",(SELECT album_id FROM album WHERE album_name="{albumname}"), (SELECT genre_id FROM genre WHERE genre_type="{genre}"))')
        conn.execute(f'INSERT INTO played(track_id,play_time) VALUES((SELECT track_id FROM track WHERE track_title="{tracktitle}"),{duration})')
        db.commit()
    except Exception as e:
        print(f"Sorry an error has occured : {e}. Please try again")



