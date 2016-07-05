import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 80
LIMIT_FPS = 20

libtcod.console_set_custom_font('lucida10x10_gs_tc.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'cybHack', False)