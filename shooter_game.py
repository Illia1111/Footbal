
from pygame import *
from random import randint

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"  
img_hero = "pngimg.png"  
img_enemy = "ufo.png"  

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        
        super().__init__()
        
        self.speed = player_speed  
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    



class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x = self.rect.x-self.speed
        if keys[K_RIGHT]:
            self.rect.x = self.rect.x+self.speed
     

lost = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y = self.rect.y + self.speed
 
        if self.rect.y >= 450:
            global lost
            lost = lost + 1
            self.rect.y = 0
            self.rect.x = randint(80,650)
            self.speed = randint(1,2)



enemy = sprite.Group()
monsters.add()

win_width = 700
win_height = 500

display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

background = transform.scale(image.load(img_back), (win_width, win_height))

run = True  
clock = time.Clock()
FPS = 60

hero = Player(img_hero,350,450,50,50,5)
font.init()
font = font.SysFont('Arial',24)

score = 0




while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
            
    window.blit(background, (0, 0))
    enemy.draw(window)
    enemy.update()

    text = font.render("XP1" + str(lost), True,(255,255,255) )
    window.blit(text,(20,20))
    
    text = font.render("XP2" + str(score), True,(255,255,255) )
    window.blit(text,(40,40))


    hero.reset()
    hero.move()
    
    



    display.update()
    clock.tick(FPS)
