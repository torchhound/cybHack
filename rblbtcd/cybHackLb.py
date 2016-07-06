import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80

playerX = SCREEN_WIDTH/2
playerY = SCREEN_HEIGHT/2

def handleKeys():
    global playerX, playerY
 
    key = libtcod.console_wait_for_keypress(True)
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE: #exit game
        return True 
 
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playerY -= 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playerY += 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerX -= 1
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerX += 1

libtcod.console_set_custom_font('lucida10x10_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'cybHack', False)

while not libtcod.console_is_window_closed():
 
    libtcod.console_set_default_foreground(0, libtcod.white)
    libtcod.console_put_char(0, playerX, playerY, '@', libtcod.BKGND_NONE)
    libtcod.console_flush()
    
    libtcod.console_put_char(0, playerX, playerY, ' ', libtcod.BKGND_NONE)
 
    #handle keys and exit game if needed
    exit = handleKeys()
    if exit:
        break