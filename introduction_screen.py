import tcod as libtcod
from input_handlers import handle_keys
import ui


def create_intro(board):
    filename = "introduction.txt"
    board = file_operations.import_board(filename)
    return board


def intro_menu_select():
 
    introduction_menu = True
    while introduction_menu:
        create_intro('introduction.txt')
        
        
        if answer == '1':
            #start game
        
        elif answer == '2':
            #display info/screen 'how to play'

        elif answer == '3':
            #quit
       
       

def create_character():
  
    
    symbols = ['@', '%', '$', '&']
   