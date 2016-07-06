import sys
import numpy as np

enemyDict = {}

def skillParse():
    return False

class entity():
    #id = ''
    hp = ''
    mp = ''
    dex = '' #dexterity
    str = '' #strength
    con = '' #constitution
    int = '' #intelligence
    wis = '' #wisdom
    char = '' #charisma
    def __init__(self, hp, mp, dex, str, con, int, wis, char):
        #self.id = id
        self.hp = hp
        self.mp = mp
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
        
        
class map():
    map = np.empty([80, 80])
    #def __init__():
    #
    def move():
    
    def create():
                
    def drawHud():
    
    def display():
         

def movement():
    userMv = sys.stdin.read(1) #detect if greater than 1 char
    if userMv == '\x1b[A' or 'w':
        print("up")
    elif userMv == '\x1b[B' or 's':
        print("down")
    elif userMv == '\x1b[C' or 'd':
        print("right")
    elif userMv == '\x1b[D' or 'a':
        print("left")
    else:
        inputParser()
        
def inputParser():
    userInput = input()
    if userInput == "help":
        print()
    if userInput == "stats":
        print(player.showStats())
    if userInput == "look":
        print()
    if userInput == "cast":
        print()
    if userInput == "inv" or "inventory":
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
    print("To move use WASD, for a command type and then press enter. Try 'help' and then hitting enter.")
    while True:
        movement()
    
if __name__=='__main__':
        gameLoop()
