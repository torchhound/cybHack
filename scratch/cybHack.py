import sys
import numpy as np
import enemies, mapGen

def skillParse():
    return False

class object(): 
    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
 
    def die(self, dx, dy):
        #set coordinates to background tile
    
class entity(object):
    #id = ''
    hp = ''
    #stamina = ''
    dex = '' #dexterity
    str = '' #strength
    con = '' #constitution
    int = '' #intelligence
    wis = '' #wisdom
    char = '' #charisma
    def __init__(self, hp, dex, str, con, int, wis, char): #id
        #self.id = id
        self.hp = hp
        self.dex = dex
        self.str = str
        self.con = con
        self.int = int
        self.wis = wis
        self.char = char
    
    def showStats(self):
        print(self.hp)
        print(self.mp)
        print(self.str)
        print(self.dex)
        print(self.con)
        print(self.int)
        print(self.wis)
        print(self.char)
    
    def changeStats(self, skill, new):
        self.skill = new

class player(entity):
    inventory = {} 
    money = ''
    classR = ""
    level = 1
    xp = ""
    global playerX, playerY
    
    def createChar(self):
        print("Type a number to choose your runner:")
        print("""
        1:Off-duty Cop

        2:Assassin

        3:Hacker

        4:Cyborg

        5:Street Samurai

        6:Punk

        """)
        userChoice = input()
        if userChoice == "1":
            self.classR = "Off-duty Cop"
            
        elif userChoice == "2":
            self.classR = "Assassin"
            
        elif userChoice == "3":
            self.classR = "Hacker"
            
        elif userChoice == "4":
            self.classR = "Cyborg"
            
        elif userChoice == "5":
            self.classR = "Street Samurai"
            
        elif userChoice == "6":
            self.classR = "Punk"
            

def movement():
    try:
        userMv = sys.stdin.read(1) #detect if greater than 1 char and pass to input parser
    except Exception: #specify?
        inputParser()
    else: 
        if userMv == '\x1b[A' or 'w': #fix arrow keys?
            playerY += 1
        elif userMv == '\x1b[B' or 's':
            playerY -= 1
        elif userMv == '\x1b[C' or 'd':
            playerX += 1
        elif userMv == '\x1b[D' or 'a':
            playerX -= 1
        
def inputParser():
    userInput = input()
    if userInput == "help":
        print()
    elif userInput == "stats":
        print(player.showStats())
    elif userInput == "look":
        print()
    elif userInput == "cast":
        print()
    elif userInput == "inv" or "inventory":
        print()
    #if userInput == "options": aliases?
    #   
    else:
        print("Unrecognized command, please try again or type help and then press enter")

def gameLoop():
    print(""" 
    _  _  _ _______        _______  _____  _______ _______      _______  _____       _______ __   __ ______  _     _ _______ _______ _     _
    |  |  | |______ |      |       |     | |  |  | |______         |    |     |      |         \_/   |_____] |_____| |_____| |       |____/ 
    |__|__| |______ |_____ |_____  |_____| |  |  | |______         |    |_____|      |_____     |    |_____] |     | |     | |_____  |    \_
                                                                                                                                         
    """)
    print("""
    The year is 2025 and megacorps have finally completed their takeover of all levels of society. The masses toil under the oppressive bootheels of the upper echelon and the
    puppet government. Runners and hackers ply their trade in the shadows, always at an uneasy impasse with the powers that be. What will you fight for?
    """)
    #character creation
    #choose mission type
    print("To move use WASD, for a command type and then press enter. Try 'help' and then hitting enter.")
    while True:
        movement()
    
if __name__=='__main__':
        gameLoop()
