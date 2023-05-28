from pygame import *
from time import sleep

mixer.init()

mixer.music.load('music.mp3')
mixer.music.play()



img_back = "back.jpg"  
img_hero = "left1.png"  
img_enemy = "right.png"  
kick = 'kick2.png'
img_bac = 'menu.jpg'


class GameSprite(sprite.Sprite):
    
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.speed = player_speed  
        self.image_l = transform.scale(image.load('left1.png'), (size_x, size_y))
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.image_r = transform.scale(image.load('right1.png'), (size_x, size_y))
        self.image_rr = transform.scale(image.load('right.png'), (size_x, size_y))
        self.image_ll = transform.scale(image.load('left.png'), (size_x, size_y))
        self.image_kk = transform.scale(image.load(kick), (size_x, size_y))
        self.image_k = transform.scale(image.load('kick3.png'), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.isJump = False
        self.jumpCount = 10
        self.lost = 100
        self.score = 100

    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def fire(self):
        bullet = Bulet('suriken.png',self.rect.centerx,self.rect.top,50,40,10 )
        bullets.add(bullet)
    def firee(self):
        bullet = Bulet('suriken.png',self.rect.centerx,self.rect.top,1,1,1 )
        bullets.add(bullet)

    def update(self):
        self.rect.y = self.rect.y + self.speed



    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10: 
                self.rect.y -= (self.jumpCount * abs(self.jumpCount)) * 0.3
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
    def kickk(self, hero):
        if self.rect.colliderect(hero.rect):
            hero.score = hero.score - 5

class Enemy(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.image  = self.image_ll
            self.rect.x = self.rect.x-self.speed
            
        if keys[K_d]:
            self.image  = self.image_rr
            self.rect.x = self.rect.x+self.speed
            
    def kick(self, enemy):
        if self.rect.colliderect(enemy.rect):
            enemy.lost = enemy.lost - 5
    
        
                



class Button(sprite.Sprite):
    def __init__(self, btn_image_name, x,y, width, height):
        self.image = transform.scale(image.load(btn_image_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

    def draw(self, window):
        action = False
        pos = mouse.get_pos()

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                
        if mouse.get_pressed()[0] == 0:
            self.clicked = False

        window.blit(self.image, (self.rect.x, self.rect.y))

        return action


    





class Bulet(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.speed = player_speed  
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def update(self):
        self.rect.x = self.rect.x - self.speed
        if self.rect.x < 0 :
            self.kill()



    

score = 100
lost = 100

bullets = sprite.Group()

btn1 = Button('start_btn.png',  int(500/2),int(700/2), 100, 50)
btn2 = Button('exit_btn.png', 300,100, 100, 50)


win_width = 700
win_height = 500

display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

background = transform.scale(image.load(img_back), (win_width, win_height))

run = False  
game = True

clock = time.Clock()
FPS = 60

enemy = Enemy(img_enemy,10,100,150,200,5)
hero = Player(img_hero,550,100,120,200,5)

enemys = sprite.Group()
enemys.add(enemy)

heros = sprite.Group()
heros.add(hero)

sco = 6000

font.init()
font = font.SysFont('Arial',24)


bu = 5
a = 10  

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
            if e.key == K_UP:
                hero.isJump = True
            if e.key == K_w:
                enemy.isJump = True
            if e.key == K_SPACE:
                if bu > 0:
                    hero.fire()
                    bu = bu - 1
            
            
            if e.key == K_h:
                enemy.kick(hero)
            if e.key == K_l:
                hero.kickk(enemy)
                
                
                

                
                
            
    if run:    
        window.blit(background, (0, 0))

        enemy.reset()
        enemy.move()
        enemy.jump()
    

        hero.jump()
        hero.reset()
        hero.move()
    
        bullets.update()
        bullets.draw(window)
    

    
        sco = sco - 1


        text = font.render("Здоров'я:" + str(hero.lost), True,(255,255,255) )
        window.blit(text,(550,20))
        text = font.render("Сюрікени:" + str(bu), True,(255,255,255) )
        window.blit(text,(550,40))
    
        text = font.render("Здоров'я:" + str(enemy.score), True,(255,255,255) )
        window.blit(text,(20,20))


        if sprite.groupcollide(enemys, bullets, False, True):
            enemy.score = enemy.score - a

        text = font.render("час:" + str(sco), True,(0,255,0) )
        window.blit(text,(250,20))

        if sco <= 0:
            text = font.render("DRAW" , True, (255,0,0))
            window.blit(text,(350,250))
            display.update()
            sleep(2)
            hero.lost = 100
            enemy.score = 100
            enemy = Enemy(img_enemy,10,100,150,200,5)
            hero = Player(img_hero,550,100,120,200,5)
            sco = 10000
            bu = 5

    
        if hero.lost <= 0 or score <= 0:
            text = font.render("YOU LOSE" , True, (255,0,0))
            window.blit(text,(325,200))
            display.update()
            sleep(1)
            hero.lost = 100
            enemy.score = 100
            enemy = Enemy(img_enemy,10,100,150,200,5)
            hero = Player(img_hero,550,100,120,200,5)
            sco = 10000
            bu = 5

        

    else:
        if btn1.draw(window):
            run = True
        if btn2.draw(window):
            game = False



    display.update()
    clock.tick(FPS)
