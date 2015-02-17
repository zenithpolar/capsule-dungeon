import libtcodpy as libtcod
import time

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

class MoveableObject(object):
    
    objects = []
    
    def __init__(self, con, x, y, char, color):
        self.con = con
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.__class__.objects.append(self)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    def draw (self):
        libtcod.console_set_default_foreground(self.con, self.color)
        libtcod.console_put_char(self.con, self.x, self.y, self.char, libtcod.BKGND_NONE)
        #libtcod.console_blit(self.con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.target_con, 0, 0)

    def clear(self):
        libtcod.console_put_char(self.con, self.x, self.y, ' ', libtcod.BKGND_NONE)
        #libtcod.console_blit(self.con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.target_con, 0, 0)
    
    @staticmethod
    def drawAll():
        for obj in MoveableObject.objects:
            obj.draw()
    
    @staticmethod
    def clearAll():
        for obj in MoveableObject.objects:
            obj.clear()
    
def handle_keys(player):
    
    key = libtcod.console_check_for_keypress(True)
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0, -1)
    
    if libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0, 1)
        
    if libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1, 0)
        
    if libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1, 0)

def main():
    libtcod.console_set_custom_font(
        'arial10x10.png',
        libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD
    )
    
    libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'capsule dungeon')
    con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

    player = MoveableObject(con, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)
    #NPC
    MoveableObject(con, SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)
    while not libtcod.console_is_window_closed():
        MoveableObject.drawAll()

        #blit the contents of "con" to the root console and present it
        libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
        libtcod.console_flush()

        MoveableObject.clearAll()

        if handle_keys(player):
            break
        time.sleep(0.093)

if __name__ == "__main__":
    main()