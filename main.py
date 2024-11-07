import pygame as pg, random as rd, os, sys

os.chdir(os.path.dirname(os.path.abspath(__file__)))

active = False
# keyboard.add_hotkey("esc", lambda: globals().update(active = not active))

pg.init()
width = 360
height = 480
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock() # not ()?

class Tiles:
    def __init__(self) -> None:
        self.list = [Tile(rd.choice(["left", "right"])) for _ in range(5)]
        self.gap = 60
        for i in range(len(self.list)):
            self.list[i].top = 260 - self.gap * i

    def get_new(self):
        self.side = rd.choice(["left", "right"])
        self.list.append(Tile(self.side))

    def draw(self):
        self.rect


class Tile:
    def __init__(self, side) -> None:
        self.side = side
        self.left = width/2 + 20 if self.side == "right" else width/2 - 100
        self.width = 80
        self.height = 14
        self.top = -self.height
        self.color = (255, 255, 255)
    
    def update(self):
        self.top += 2

    def draw(self):
        rect = pg.Rect(self.left, self.top, self.width, self.height)
        pg.draw.rect(screen, self.color, rect)

class Player:
    def __init__(self) -> None:
        self.width = 20
        self.height = 20
        self.left = width / 2 - self.width / 2
        self.top = 400
        self.color = (255, 255, 0)
        self.count = 0

    def draw(self):
        rect = pg.Rect(self.left, self.top, self.width, self.height)
        pg.draw.rect(screen, self.color, rect)

    def update(self):
        self.top += 2
    
    def jump(self):
        n_tile = tiles.list[self.count]
        self.left = width / 2 - 60 - self.width / 2 if  n_tile.side == "left" else width / 2 + 60 - self.width / 2
        self.top = n_tile.top - self.height
        self.count += 1
    
    def die(self):
        n_tile = tiles.list[self.count]
        self.left = width / 2 + 60 - self.width / 2 if  n_tile.side == "left" else width / 2 - 60 - self.width / 2
        self.top = n_tile.top - self.height


tiles = Tiles()
player = Player()
# print(tiles.start_tiles)

while True:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_ESCAPE:
                active = not active
            if e.key == pg.K_LEFT:
                active = True
                if tiles.list[player.count].side == "left":
                    player.jump()
                else:
                    active = False
                    player.die()
            if e.key == pg.K_RIGHT:
                active = True
                if tiles.list[player.count].side == "right":
                    player.jump()
                else:
                    active = False
                    player.die()

    screen.fill((0,0,0))
    if active:
        for tile in tiles.list:
            tile.update()
        player.update()

        if tiles.list[-1].top >= tiles.gap:
            tiles.get_new()

    for tile in tiles.list:
        tile.draw()
    player.draw()
    pg.display.flip()
    clock.tick(60)

    