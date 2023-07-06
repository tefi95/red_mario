from pygame import *

BLACK = (0, 0, 0)
WIDTH = 700
HEIGHT = 500
FPS = 60
screen = display.set_mode((700, 500))
display.set_caption('Подземелье')
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
        
        if keys_pressed[K_SPACE]:
            self.rect.y -= 10
            self.rect.y += 15 
        
        # if keys_pressed[K_SPACE]:
        #     self.rect.y += 10


player = Player('a1.png', 20, 300, 20)


class Enemy(GameSprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__(image, player_x, player_y, speed)
        self.right = True


game = True
monetka = GameSprite('treasure.png', 620, 300, 20)
demon_1 = Enemy('Canine.png', 200, 250, 20)
demon_2 = Enemy('Canine_2.png', 500, 330, 20)

#игровой цикл
while game:
    clock.tick(FPS)
    screen.blit(background, ((0, 0)))
    player.update()
    monetka.update()
    demon_1.update()
    demon_2.update()

    player.reset()
    monetka.reset()
    demon_1.reset()
    demon_2.reset()

    #работа с событиями
    for e in event.get():
        # проверить закрытие окна
        if e.type == QUIT:
            game = False


    
    display.update()