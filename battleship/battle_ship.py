#!/usr/bin/python3
#Ella Adam and Rupak Kannan
#3/6/2020

import tkinter as tk
from tkinter import scrolledtext 
from tkinter import dnd
import random as rd
from tkinter import dnd

#global variables
DEFAULT = ("Arial", 15)

class Screen(tk.Frame):
    current = 0
    def __init__(self):
        tk.Frame.__init__(self)
        
    def switch_frame():
        screens[Screen.current].tkraise()
        #print(Screen.current)
        
class MainMenu(tk.Frame):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "BATTLE SHIP", font = ("Arial", 20))
        self.lbl_title.grid(row = 0, column = 0, columnspan = 3, sticky = "news")
        
        self.btn_play = tk.Button(self, text = "PLAY", font = DEFAULT, command = self.player_setup)
        self.btn_play.grid(row = 1, column = 0,  columnspan = 3, sticky = "news")
        
        self.btn_play = tk.Button(self, text = "HOW TO PLAY", font = DEFAULT, command = self.help)
        self.btn_play.grid(row = 2, column = 0,  columnspan = 3, sticky = "news")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
    def help(self):
        popup = tk.Tk()
        popup.title("Help")
        root.withdraw()
        frm_help = Help(popup)
        frm_help.grid(row = 0, column = 0)
        
    def player_setup(self):
        
        Screen.current = 1
        Screen.switch_frame()        
    
class Help(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        #Creating Scolled Test
    
        scroll_width = 40
        scroll_height = 8
    
        self.scroll = scrolledtext.ScrolledText(self, width = scroll_width, height = scroll_height,
                                               wrap = tk.WORD)
        
        self.scroll.grid(row = 1, column = 0)        
        help_text = """Game Objective:
        
The object of Battleship is to try and sink all of the other player's before they sink all of your ships. All of the other player's ships are somewhere on his/her board.  You try and hit them by calling out the coordinates of one of the squares on the board.  The other player also tries to hit your ships by calling out coordinates.  Neither you nor the other player can see the other's board so you must try to guess where they are.  Each board in the physical game has two grids:  the lower (horizontal) section for the player's ships and the upper part (vertical during play) for recording the player's guesses.

Starting a New Game
Each player places the 5 ships somewhere on their board.  The ships can only be placed vertically or horizontally. Diagonal placement is not allowed. No part of a ship may hang off the edge of the board.  Ships may not overlap each other.  No ships may be placed on another ship. 

Once the guessing begins, the players may not move the ships.

The 5 ships are:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).  

Playing the Game
Player's take turns guessing by calling out the coordinates. The opponent responds with "hit" or "miss" as appropriate.  Both players should mark their board with pegs:  red for hit, white for miss. For example, if you call out F6 and your opponent does not have any ship located at F6, your opponent would respond with "miss".  You record the miss F6 by placing a white peg on the lower part of your board at F6.  Your opponent records the miss by placing.

When all of the squares that one your ships occupies have been hit, the ship will be sunk.   You should announce "hit and sunk".  In the physical game, a red peg is placed on the top edge of the vertical board to indicate a sunk ship. As soon as all of one player's ships have been sunk, the game ends."""
        
        self.scroll.insert("insert", help_text)
    
        self.btn_cancel = tk.Button(self, text = "Back", font = DEFAULT, command = self.ressurect)
        self.btn_cancel.grid(row = 2, column = 0)
        
    def ressurect(self):
        self.parent.destroy()
        root.deiconify()
    
class Computer(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent
        
        for i in range(6):
            self.grid_columnconfigure(i, weight = 1)

        Computer_rows = 5
        Computer_columns = 5
        
        for x in range(Computer_rows):
            for i in range(Computer_columns):
                self.btn_spot = tk.Button(self)
                self.btn_spot.grid(row = i+1, column = x, sticky = "news")      
        
        self.lbl_computer = tk.Label(self, text = "Computer", font = ("Arial", 20))
        self.lbl_computer.grid(row = 0, column = 1, columnspan = 3, sticky = "news")        
            
        self.lbl_blank = tk.Label(self, text = "-------------------------------------------------------")
        self.lbl_blank.grid(row = 6, column = 0, sticky = "news", columnspan = 5)        
                
           

        
class Player(tk.Frame):
    def __init__(self):
        Screen.__init__(self)
        
        for i in range(7):
            self.grid_columnconfigure(i, weight = 1)

        Player_rows = 5
        Player_columns = 5
         
        for x in range (Player_rows):
            for i in range(Player_columns):
                self.btn_spot = tk.Button(self)
                self.btn_spot.grid(row = i+1, column = x, sticky = "news")              
            
        self.lbl_player = tk.Label(self, text = "Player", font = ("Arial", 20))
        self.lbl_player.grid(row = 0, column = 0, columnspan = 5, sticky = "news")
        
        
        self.lbl_blank = tk.Label(self, text = "-------------------------------------------------------")
        self.lbl_blank.grid(row = 6, column = 0, columnspan = 5)        
        
        self.btn_done = tk.Button(self, text = "Done", font = DEFAULT, command = self.show)
        self.btn_done.grid(row = 7, column = 0, columnspan = 5)
        
    def show(self):
        popup = tk.Tk()
        popup.title("BattleShip")
        self.btn_done.destroy()
        frm_comp = Computer(popup)
        frm_comp.grid(row = 0, column = 0) 
        popup.resizable(False, False)
   
if __name__ == "__main__":
    root = tk.Tk()
    root.title("BattleShip")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight=1)
    
    #MainMenu --> screens[0]

    screens = [MainMenu(), Player()]
    
    screens[0].grid(row = 0, column = 0, sticky = "news")    
    screens[1].grid(row = 0, column = 0, sticky = "news")

    Screen.current = 0
    Screen.switch_frame()
    
    
root.resizable(False, False)
root.mainloop()