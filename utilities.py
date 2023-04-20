from menu import Menu
from menu import player2
from menu import player1
import sqlite3

EMPTY_CELL = ' '
BOARD = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1
WIN = 1    
DRAW = -1    
Running = 0    
Stop = 1      
Game = Running    



def show_menu():
    for choice in Menu:
        print(f'{choice.value}.{choice.name.replace("_"," ")}')

def connect_to_database(database_name):
    connection = sqlite3.connect(database_name)
    return connection


db_connection = connect_to_database('database.db')


def get_user_choice():
  while True:
    show_menu()
    user_choice = input("Enter a choice, from 1 to 4: ")
    for menu_item in Menu:
        if menu_item.value == user_choice:
            return user_choice
   
    print("Invalid choice")
    continue

def Board(): 

    print((BOARD[1],BOARD[2],BOARD[3]))    
  
    print( (BOARD[4],BOARD[5],BOARD[6]))    
  
    print( (BOARD[7],BOARD[8],BOARD[9]))

    print('____________________________')

def Check_Position(x):    
    if(BOARD[x] == ' '):    
        return True    
    else:    
        return False

def game_play():
    
    def WIN_DECISION():
        global Game   

        if (BOARD[1] == BOARD[2] == BOARD[3] and BOARD[1] != ' '):    
            Game = WIN    

        elif (BOARD[4] == BOARD[5] == BOARD[6] and BOARD[4] != ' '):    
            Game = WIN   

        elif (BOARD[7] == BOARD[8] == BOARD[9] and BOARD[7] != ' '):    
            Game = WIN    
    
        elif (BOARD[1] == BOARD[4]  == BOARD[7] and BOARD[1] != ' '):    
            Game = WIN    

        elif (BOARD[2] == BOARD[5] == BOARD[8] and BOARD[2] != ' '):    
            Game = WIN    

        elif (BOARD[3] == BOARD[6] == BOARD[9] and BOARD[3] != ' '):    
            Game=WIN    
    
        elif (BOARD[1] == BOARD[5] == BOARD[9] and BOARD[5] != ' '):    
            Game = WIN    

        elif (BOARD[3] == BOARD[5] == BOARD[7] and BOARD[5] != ' '):    
            Game=WIN    

        elif (BOARD[1]!=' ' and BOARD[2]!=' ' and BOARD[3]!=' ' and BOARD[4]!=' ' and BOARD[5]!=' ' and BOARD[6]!=' ' and BOARD[7]!=' ' and BOARD[8]!=' ' and BOARD[9]!=' '):    
            Game=DRAW    

        else:            
            Game=Running    
        
    player = 1
    while(Game == Running):    

        Board()    
        if(player % 2 != 0):    
            print(f"{player1} turn")    
            Mark = 'X'    
        else:    
            print(f"{player2} turn")    
            Mark = 'O'    

        choice = int(input("Enter the position between [1-9] where you want to mark : "))    
        if(Check_Position(choice)): 
            BOARD[choice] = Mark    
            player+=1    
            WIN_DECISION()    
        

    Board()    
    if(Game==DRAW):    
        print("Game Draw")
        with open("data.txt", "w") as file:
            file.write("This Game was a draw")
            file.write("\n") 

    elif(Game==WIN):    
        player-=1    
        if(player % 2 !=0):    
            print(f"{player1} Won")
            with open("data.txt", "w") as file:
                file.write(f"{player1} Won")
                file.write("\n") 
            # Update a number of wins in a table
            cursor = db_connection.cursor()
            cursor.execute("UPDATE Record SET wins = wins + ? WHERE name = ?", (1, player1))
            db_connection.commit()
            # Close connection
            db_connection.close()
             
        else:    
            print(f"{player2} Won")
            with open("data.txt", "w") as file:
                file.write(f"{player2} Won")
                file.write("\n") 
            # Update a number of wins in a table
            cursor = db_connection.cursor()
            cursor.execute("UPDATE Record SET wins = wins + ? WHERE name = ?", (1, player2))
            db_connection.commit()
            # Close connection
            db_connection.close()

def load_data():
    with open("data.txt", "r") as file:
        plays = file.readline
        for line in file:
            print(line)
            return line
        




