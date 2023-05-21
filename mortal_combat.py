
from pygame import *



img_back = "back.jpg"  
img_hero = "right1.png"  
img_enemy = "left.png"  

class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.speed = player_speed  
        self.image_l = transform.scale(image.load('left1.png'), (size_x, size_y))
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.image_r = transform.scale(image.load('right1.png'), (size_x, size_y))
        self.image_rr = transform.scale(image.load('right.png'), (size_x, size_y))
        self.image_ll = transform.scale(image.load('left.png'), (size_x, size_y))
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.isJump = False
        self.jumpCount = 10

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10: 
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10  



class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.image  = self.image_l
            self.rect.x = self.rect.x-self.speed
        if keys[K_RIGHT]:
            self.image  = self.image_r
            self.rect.x = self.rect.x+self.speed




     

class Enemy(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.image  = self.image_ll
            self.rect.x = self.rect.x-self.speed
        if keys[K_d]:
            self.image  = self.image_rr
            self.rect.x = self.rect.x+self.speed
    def kick(self):
        keys = key.get_pressed()
        if keys[K_g]:
            pass
           









win_width = 700
win_height = 500

display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

background = transform.scale(image.load(img_back), (win_width, win_height))

run = True  
clock = time.Clock()
FPS = 60

enemy = Enemy(img_enemy,550,100,150,200,5)
hero = Player(img_hero,10,100,120,200,5)

font.init()
font = font.SysFont('Arial',24)






while run:
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.isJump = True
            
    window.blit(background, (0, 0))

    enemy.reset()
    enemy.move()
    hero.jump()
    hero.reset()
    hero.move()
    
    



    display.update()
    clock.tick(FPS)
