import utilities
import os
import sqlite3

welcome_msg = """
===========================================
==== Welcome to TIC-TAC-TOE ====
===========================================
"""

print(welcome_msg)

def connect_to_database(database_name):
    connection = sqlite3.connect(database_name)
    return connection


db_connection = connect_to_database('database.db')
db_connection = connect_to_database('database.db')



if os.path.exists("data.txt"):
  utilities.load_data()

while True:
  choice = utilities.get_user_choice()

  if choice == utilities.Menu.NEW_GAME.value:
    choice = utilities.game_play()    
    print('Please exit and start again to play more')

  elif choice == utilities.Menu.GAME_HISTORY.value:
    choice = utilities.load_data()
   
  elif choice == utilities.Menu.PLAYER_RECORD.value:
    print("Listing Accounts ... ")
    # Retrive all data from the table
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM Record")
    db_connection.commit()

    # Closing the connection
    db_connection.close()

    
  elif choice == utilities.Menu.EXIT.value:
    print("Exiting ... ")
    break
