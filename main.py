import mysql.connector
import users
import insert_track
import display
import delete
import update
import search
import playlist



HOSTNAME = 'localhost'
USERNAME = 'root'
PASSWORD = 'pranita5'
DATABASE = 'music_library_management'

mydb = mysql.connector.connect(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, db=DATABASE)
conn = mydb.cursor()


if __name__ == '__main__':
    
    print("WELCOME TO THE MUSIC LIBRARY MANAGEMENT SYSTEM\n")
    u_input=input("Please enter Y to login or enter N to exit\n")
    if(u_input=='Y'):
        users.login()
        choice=1
        
        while True:
            choice=int(input("Please enter 0 to exit or enter 1 to continue\n"))
            if choice==0:
                print("Exiting...\n")
                print("Thank you !!\n Hope to see you again !")
                break
            else:
                x=int(input("Select:\n 1. To enter a song into the database\n 2. To display all the songs in the database\n 3. To delete a song\n 4. To update a song existing in the database\n 5. To search for a song in the database\n 6. To create your own playlist\n"))
                if(x==1):
                    insert_track.insert()
                    print("Your song has been sucessfully added SS!\n")
                elif x==2:
                    display.display()
                elif x==3:
                    delete.delete()
                elif x==4:
                    update.update()
                elif x==5:
                    search.search()
                elif x==6:
                    playlist.playlist()
            
                 
    else:
        print("Hope to see you again ! \n")


    
    

