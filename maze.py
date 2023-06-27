# создай игру "Лабиринт"!
from pygame import *

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()


BLACK = (0, 0, 0)
WIDTH = 700
HEIGHT = 500
FPS = 60
screen = display.set_mode((700, 500))
display.set_caption('Лабиринт')
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

background = transform.scale(image.load('background.jpg'), (700, 500))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 640:
            self.rect.x += self.speed

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

class Enemy(GameSprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__(image, player_x, player_y, speed)
        self.right = True

    def update(self):
        if self.rect.x >= 530 and not self.right:
            self.rect.x -= self.speed
            if self.rect.x <= 530:
                self.right = True


        elif self.rect.x <= 650 and self.right:
            self.rect.x += self.speed
            if self.rect.x >= 650:
                self.right = False


class Wall(sprite.Sprite):
    def __init__(
        self, 
        color: tuple,
        wall_x: int,
        wall_y: int,
        wall_width: int, 
        wall_height: int,
        screen: Surface,
    ):
        super().__init__()
        self.color = color
        self.width = wall_width
        self.height = wall_height
        # картика стены - прямоугольник нужных размеров и цвета
        self.image = Surface((self.width, self.height))
        self.image.fill(color)
        # каждый спрайт должен хранить свойство rect - прямоугольник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
        self.screen = screen

    def draw_wall(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

hero = Player('hero1.png', 500, 400, 4)
cyborg = Enemy('cyborg.png', 600, 400, 2)
final = GameSprite('treasure.png', 25, 20, 0)
w1 = Wall(BLACK, 40, 200, 25, 400, screen)
w2 = Wall(BLACK, 250, 300, 25, 300, screen)
w3 = Wall(BLACK, 400, 150, 25, 350, screen)
w4 = Wall(BLACK, 270, 0, 25, 200, screen)
w5 = Wall(BLACK, 150, 0, 25, 320, screen)
w6 = Wall(BLACK, 550, 0, 25, 300, screen)


x1 = 400
y1 = 400

x2 = 100
y2 = 100

finish = False
game = True

font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN!", True, (255, 215, 0))
lose = font.render("YOU LOSE!", True, (180, 0, 0))

while game:
    clock.tick(FPS)

    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        hero.update()
        cyborg.update()
        final.update()

        screen.blit(background, ((0, 0)))
        hero.reset()
        cyborg.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()

    if (
        sprite.collide_rect(hero, cyborg)
        or sprite.collide_rect(hero, w1)
        or sprite.collide_rect(hero, w2)
        or sprite.collide_rect(hero, w3)
        or sprite.collide_rect(hero, w4)
        or sprite.collide_rect(hero, w5)
        or sprite.collide_rect(hero, w6)

    ):
        finish = True
        screen.blit(lose, (200, 200))
        kick = mixer.Sound('kick.ogg')
        kick.play()
    
    if sprite.collide_rect(hero, final):
        finish = True
        screen.blit(win, (200, 200))
        money = mixer.Sound('money.ogg')
        money.play()

        
    
    display.update()