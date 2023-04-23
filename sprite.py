from pygame import*


class GameSprite(sprite.Sprite):
    def __init__(self, img_name, width, height, x, y)
    self.image = transform.scale(image.load(image.name), (width, height))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

def draw(self, window):
    window.blt(self.image, (self.rect.x, self.rect.y))


class Player1(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= 5
        if keys[K_RIGHT]:
            self.rect.x += 5
        if keys[K_DOWN]:
            self.rect.y -= 5
        if keys[K_UP]:
            self.rect.y += 5

class Player2(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_Q]:
            self.rect.x -= 5
        if keys[K_E]:
            self.rect.x += 5
        if keys[K_S]:
            self.rect.y -= 5
        if keys[K_W]:
            self.rect.y += 5


class Fire(GameSprite):
    def shoot(self)

    




    
