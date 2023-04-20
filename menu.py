from enum import Enum
import sqlite3
alphabetic_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                                                                                                                          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

MIN_LENGTH = 3
MAX_LENGTH = 12
      

class Menu(Enum):
    NEW_GAME = "1"
    GAME_HISTORY = "2"
    PLAYER_RECORD = "3"
    EXIT = "4"



def name_validator(name1, name2):
    while True:

        if (len(name1)<MIN_LENGTH):
            print("Length must be between 3 and 12 characters")

        if (len(name2)>MAX_LENGTH):
            print("Length must be between 3 and 12 characters")   

        elif (len(name1)<MIN_LENGTH):
            print("Length must be between 3 and 12 characters")

        elif (len(name2)>MAX_LENGTH):
            print("Length must be between 3 and 12 characters")   

        else:
            # return player2, player1
            break



player1 = input("Enter a username(you will play has X:")
player2 = input("Enter a username(you will play has O:")


name_validator(name1=player1, name2=player2)



def connect_to_database(database_name):
    connection = sqlite3.connect(database_name)
    return connection


db_connection = connect_to_database('database.db')

# Insert name into the table
cursor = db_connection.cursor()
cursor.execute("INSERT INTO Record (name) VALUES (?)", (player1,))
cursor.execute("INSERT INTO Record (name) VALUES (?)", (player2,))
db_connection.commit()

# Closing the connection
db_connection.close()


