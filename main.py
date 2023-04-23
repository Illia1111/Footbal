from pygame import *
from button import Button 
from sprite import Player, GameSprite


bg = transform.scale(image.load(), (700,500))

run = False
game = True







game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if run:
        window.blit(bg, (0,0))
        player.draw(window)
        player.move()
        player.jump()


    else:
        window.fill((0,0,0))
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False

    display.update()
    clock.tick(60)