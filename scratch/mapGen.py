import numpy as np

class map():
    map = np.empty([80, 80])
    def create(): #dungeon creation
    
    def dialog(text):
        print(text)
                
    def drawHud(name, player):
        print("%s  hp:%s lvl:%s xp:%s brouzef:%s" %name %player.hp %player.level %player.xp %player.money)
        print("dex:%s str:%s con:%s int:%s wis:%s char:%s" %player.dex %player.str %player.con %player.int %player.wis %player.char)
    
    def display():
        dialog(text)
        print map
        drawHud()