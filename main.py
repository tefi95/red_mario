from pygame import *

BLACK = (0, 0, 0)
WIDTH = 700
HEIGHT = 500
FPS = 60
screen = display.set_mode((700, 500))
display.set_caption('Red Mario')
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.screen = screen


    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

background = transform.scale(image.load('fon.jpg'), (700, 500))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed
        
player = Player('gg.png', 20, 300, 20)


class Enemy(GameSprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__(image, player_x, player_y, speed)
        self.right = True

    def update(self):
        self.rect.y += self.speed


game = True

#игровой цикл
while game:
    clock.tick(FPS)
    screen.blit(background, ((0, 0)))
    player.update()

    player.reset()

    #работа с событиями
    for e in event.get():
        # проверить закрытие окна
        if e.type == QUIT:
            game = False


    
    display.update()