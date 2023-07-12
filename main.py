from pygame import *

# создание окна
# ширина 
WIDTH = 700
# высота 
HEIGHT = 500
# количество кадров
FPS = 60
screen = display.set_mode((700, 500))
# название игры
display.set_caption('Подземелье')
clock = time.Clock()
# цвет стен
BLACK = (0, 0, 0)
RED = (255, 0, 255)

# музыка
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()


# главный класс
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.screen = screen
        self.speed_down = 1


    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

# нужно
go_left = True 
go_right = True
down = True
go_space = True

# класс игрока
class Player(GameSprite):
    def update(self):
        self.move_left(go_left)
        self.move_right(go_right)
        self.prityazhenie(down)
        self.move_space(go_space)

    # движение влево
    def move_left(self, a):
        keys_pressed = key.get_pressed()
        if a == True:
            if keys_pressed[K_LEFT] and self.rect.x > 5:
                self.rect.x -= self.speed

    # движение вправо
    def move_right(self, b):
        keys_pressed = key.get_pressed()
        if b == True:
            if keys_pressed[K_RIGHT] and self.rect.x < 640:
                self.rect.x += self.speed

    # прыжок
    def move_space(self, c):
        keys_pressed = key.get_pressed()
        if c == True:
            if keys_pressed[K_SPACE]:
                self.rect.y -= 100
            # s elf.rect.y += 15

    # притяжение
    def prityazhenie(self, down):
        if down == True:
            self.rect.y += self.speed_down 

# класс противника
class Enemy(GameSprite):
    def __init__(self, image, player_x, player_y, speed):
        super().__init__(image, player_x, player_y, speed)
        self.right = True

# класс стен
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



game = True
finish = False
# создание игрока,фона, приза и врагов
background = transform.scale(image.load('fon.jpg'), (700, 500))
player = Player('a1.png', 20, 320, 5)
monetka = GameSprite('treasure.png', 620, 300, 20)
demon_1 = Enemy('Canine.png', 200, 250, 1)
demon_2 = Enemy('Canine_2.png', 500, 330, 1)
# создание стен 
w1 = Wall(RED, 0, 390, 200, 10, screen)
w2 = Wall(RED, 115, 325, 10, 60, screen)
w3 = Wall(RED, 115, 325, 50, 10, screen)
w4 = Wall(RED, 160, 300, 10, 100, screen)
w5 = Wall(RED, 160, 300, 160, 10, screen)
w6 = Wall(RED, 320, 320, 10, 200, screen)
w7 = Wall(RED, 410, 330, 10, 1000, screen)
w8 = Wall(RED, 410, 330, 55, 10, screen)
w9 = Wall(RED, 460, 330, 10, 1000, screen)
w10 = Wall(RED, 520, 390, 10, 1000, screen)
w11 = Wall(RED, 520, 390, 40, 10, screen)
w12 = Wall(RED, 560, 390, 10, 1000, screen)
w13 = Wall(RED, 610, 360, 100, 10, screen)
w14= Wall(RED, 610, 360, 10, 1000, screen)
w15 = Wall(BLACK, 190, 240, 60, 10, screen)
w16 = Wall(BLACK, 500, 320, 60, 10, screen)
w17 = Wall(BLACK, 320, 500, 50, 10, screen)

# надпииси при поражении и победе
font.init()
font = font.Font(None, 70)
win = font.render("Ты победил!", True, (255, 215, 0))
lose = font.render("Попробуй снова!", True, (180, 0, 0))

#игровой цикл
while game:
    clock.tick(FPS)
    screen.blit(background, ((0, 0)))
    
    #работа с событиями
    for e in event.get():
        # проверить закрытие окна
        if e.type == QUIT:
            game = False

    # вывод играка, врага, стен и фона
    if finish != True:
        player.update()
        demon_1.update()
        demon_2.update()
        monetka.update()

        screen.blit(background, ((0, 0)))
        player.reset()
        demon_1.reset()
        demon_2.reset()
        monetka.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()
        w9.draw_wall()
        w10.draw_wall()
        w11.draw_wall()
        w12.draw_wall()
        w13.draw_wall()
        w14.draw_wall()
        w15.draw_wall()
        w16.draw_wall()
        w17.draw_wall()

    # столкновение с врагом и стеной - проигрыш
    if (
        sprite.collide_rect(player, demon_1)
        or sprite.collide_rect(player, demon_2)
        or sprite.collide_rect(player, w17)        
    ):
        finish = True
        screen.blit(lose, (200, 200))
        # музыка про проигрыше
        kick = mixer.Sound('defeat.mp3')
        kick.play()
    
    # столкновение с призом - победа
    if sprite.collide_rect(player, monetka):
        finish = True
        screen.blit(win, (200, 200))
        # музыка при победе
        money = mixer.Sound('money.ogg')
        money.play()

    # столкновение со стеной, нельзя пройти упасть вниз
    if (
        sprite.collide_rect(player, w1)
        or sprite.collide_rect(player, w3)
        or sprite.collide_rect(player, w5)
        or sprite.collide_rect(player, w8)
        or sprite.collide_rect(player, w9)
        or sprite.collide_rect(player, w12)
        or sprite.collide_rect(player, w14)
        or sprite.collide_rect(player, w15)
        or sprite.collide_rect(player, w16)
    ):
        player.speed_down = 0
        go_space = True
    else:
        player.speed_down = 1
        go_space = False

    # нельзя пройти сквозь стены - вправо
    if (
        sprite.collide_rect(player, w2)
        or sprite.collide_rect(player, w4)
        or sprite.collide_rect(player, w7)
        or sprite.collide_rect(player, w10)
        or sprite.collide_rect(player, w13)
    ):
        go_right = False
    else:
        go_right = True

    # нельзя пройти сквозь стены - влево
    if (
        sprite.collide_rect(player, w6)
        or sprite.collide_rect(player, w9)
        or sprite.collide_rect(player, w12)
    ):
        go_left = False
    else:
        go_left = True

    display.update()