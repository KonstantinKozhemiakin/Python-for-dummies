print('''
#1. «Вы победили!»
Когда человечек доберется до двери, выводите сообщение «Вы победили!». 
(Вспомните, как делали то же самое, печатая «Конец игры» для созданной в 
главе 14 игры «Прыг-скок!».)
#2. Анимация двери
В главе 15 мы создали два изображения двери — открытую 
и закрытую. Когда человечек в нее войдет, изображение должно поменяться 
(с закрытой двери на открытую). Затем человечек должен исчезнуть, 
а дверь закрыться. Тогда возникнет иллюзия, что наш герой открывает дверь, 
заходит и закрывает ее за собой. Измените для этого код классов DoorSprite
и StickFigureSprite.
#3. Движущиеся платформы
Создайте новый класс для движущихся платформ — MovingPlatform
Sprite. Они должны непрерывно перемещаться по горизонтали 
(от левой стороны игрового экрана до правой и обратно), из-за чего человечку 
будет сложнее добраться до выхода.

''')

from tkinter import *
import random
import time


class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Человечек спешит к выходу")
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(self.tk, width=500, height=500, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height = 500
        self.canvas_width = 500
        self.bg = PhotoImage(file="stickman\\background.gif")
        self.bg2 = PhotoImage(file="stickman\\background2.gif")
        self.bg3 = PhotoImage(file="stickman\\background3.gif")
        self.bg4 = PhotoImage(file="stickman\\background4.gif")
        self.bgr = [self.bg, self.bg2, self.bg3, self.bg4]
        w = self.bg.width()
        h = self.bg.height()
        for x in range(0, 5):
            for y in range(0, 5):
                random.shuffle(self.bgr)
                self.canvas.create_image(x * w, y * h, image=self.bgr[0], anchor='nw')
        self.sprites = []
        self.running = True

    def mainloop(self):
        while True:
            if self.running == True:
                for sprite in self.sprites:
                    sprite.move()
            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.02)


class Coords:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


def within_x(co1, co2):
    if (co1.x1 > co2.x1 and co1.x1 < co2.x2) \
            or (co1.x2 > co2.x1 and co1.x2 < co2.x2) \
            or (co2.x1 > co1.x1 and co2.x1 < co1.x2) \
            or (co2.x2 > co1.x1 and co2.x2 < co1.x2):
        return True
    else:
        return False


def within_y(co1, co2):
    if (co1.y1 > co2.y1 and co1.y1 < co2.y2) \
            or (co1.y2 > co2.y1 and co1.y2 < co2.y2) \
            or (co2.y1 > co1.y1 and co2.y1 < co1.y2) \
            or (co2.y2 > co1.y1 and co2.y2 < co1.y2):
        return True
    else:
        return False


def collided_left(co1, co2):
    if within_y(co1, co2):
        if co1.x1 <= co2.x2 and co1.x1 >= co2.x1:
            return True
    return False


def collided_right(co1, co2):
    if within_y(co1, co2):
        if co1.x2 >= co2.x1 and co1.x2 <= co2.x2:
            return True
    return False


def collided_top(co1, co2):
    if within_x(co1, co2):
        if co1.y1 <= co2.y2 and co1.y1 >= co2.y1:
            return True
    return False


def collided_bottom(y, co1, co2):
    if within_x(co1, co2):
        y_calc = co1.y2 + y
        if y_calc >= co2.y1 and y_calc <= co2.y2:
            return True
    return False


class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None

    def move(self):
        pass

    def coords(self):
        return self.coordinates

    def you_win(self):
        pass


class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, \
                                              image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + width, y + height)


class MovingPlatformSprite(Sprite):
    def __init__(self, game, x1, y1):
        Sprite.__init__(self, game)
        self.image_all = [
            PhotoImage(file="stickman\\platform1.gif"),
            PhotoImage(file="stickman\\platform2.gif"),
            PhotoImage(file="stickman\\platform3.gif")]
        random.shuffle(self.image_all)
        self.my_image = self.image_all[0]
        self.x = random.choice([-2, 2])
        self.y = 0
        w = self.my_image.width()
        h = self.my_image.height()
        self.image = game.canvas.create_image(x1, y1, image=self.my_image, anchor='nw')
        self.coordinates = Coords(x1, y1, x1 + w, y1 + h)

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + self.my_image.width()
        self.coordinates.y2 = xy[1] + self.my_image.height()
        return self.coordinates

    def move(self):
        co = self.coords()
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = -2
        elif self.x < 0 and co.x1 <= 0:
            self.x = +2
        self.game.canvas.move(self.image, self.x, self.y)


class RandomMovingPlatformSprite(MovingPlatformSprite):

    def __init__(self, game):
        MovingPlatformSprite.__init__(self, game, 0, 0)
        self.image_all = [
            PhotoImage(file="stickman\\platform1.gif"),
            PhotoImage(file="stickman\\platform2.gif"),
            PhotoImage(file="stickman\\platform3.gif")]
        random.shuffle(self.image_all)
        self.my_image = self.image_all[0]
        self.x = random.choice([-2, 2])
        self.y = 0
        w = self.my_image.width()
        h = self.my_image.height()
        x = random.randint(0, (self.game.canvas_width - w))
        y = random.randint(0, (self.game.canvas_height - h))
        self.image = game.canvas.create_image(x, y, image=self.my_image, anchor='nw')
        self.coordinates = Coords(x, y, x + w, y + h)


class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.images_left = [
            PhotoImage(file="stickman\\figure-L1.gif"),
            PhotoImage(file="stickman\\figure-L2.gif"),
            PhotoImage(file="stickman\\figure-L3.gif")]
        self.images_right = [
            PhotoImage(file="stickman\\figure-R1.gif"),
            PhotoImage(file="stickman\\figure-R2.gif"),
            PhotoImage(file="stickman\\figure-R3.gif")]
        self.image = game.canvas.create_image(200, 470, image=self.images_left[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = Coords()
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)

    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2

    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2

    def jump(self, evt):
        if self.y == 0:
            self.y = -4
            self.jump_count = 0

    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, \
                                            image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image, \
                                            image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, \
                                            image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image, \
                                            image=self.images_right[self.current_image])

    def coords(self):
        xy = self.game.canvas.coords(self.image)
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates

    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count -= 1
        co = self.coords()
        left = True
        right = True
        top = True
        bottom = True
        falling = True
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False
        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False
        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and collided_top(co, sprite_co):
                self.y = -self.y
                top = False
            if bottom and self.y > 0 and collided_bottom(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False
            if bottom and falling and self.y == 0 \
                    and co.y2 < self.game.canvas_height \
                    and collided_bottom(1, co, sprite_co):
                falling = False
            if left and self.x < 0 and collided_left(co, sprite_co):
                self.x = 0
                left = False
                if sprite.endgame:
                    self.game.running = False
                    for sprite in self.game.sprites:
                        sprite.you_win()
            if right and self.x > 0 and collided_right(co, sprite_co):
                self.x = 0
                right = False
                if sprite.endgame:
                    self.game.running = False
                    for sprite in self.game.sprites:
                        sprite.you_win()
        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = 4
        self.game.canvas.move(self.image, self.x, self.y)

    def you_win(self):
        self.game.canvas.itemconfig(self.image, state='hidden')
        time.sleep(0.05)
        self.game.canvas.create_text(250, 250, text='You Win!!!', font=('Helvetica', 20))


class DoorSprite(Sprite):
    def __init__(self, game, x, y):
        Sprite.__init__(self, game)
        self.photo_image = PhotoImage(file="stickman\\door1.gif")
        self.photo_image2 = PhotoImage(file="stickman\\door2.gif")
        w = self.photo_image.width()
        h = self.photo_image.height()
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = Coords(x, y, x + (w / 3), y + h)
        self.endgame = True

    def you_win(self):
        self.game.canvas.itemconfig(self.image, image=self.photo_image2)
        self.game.canvas.update()
        time.sleep(0.03)
        self.game.canvas.itemconfig(self.image, image=self.photo_image)


g = Game()
platform_1 = PlatformSprite(g, PhotoImage(file="stickman\\platform1.gif"), 10, 40, 100, 10)
platform_2 = MovingPlatformSprite(g, 75, 100)
platform_3 = MovingPlatformSprite(g, 100, 150)
platform_4 = MovingPlatformSprite(g, 150, 200)
platform_5 = PlatformSprite(g, PhotoImage(file="stickman\\platform1.gif"), 200, 250, 100, 10)
platform_6 = MovingPlatformSprite(g, 250, 300)
platform_7 = MovingPlatformSprite(g, 350, 350)
platform_8 = PlatformSprite(g, PhotoImage(file="stickman\\platform1.gif"), 400, 450, 100, 10)
platform_9 = MovingPlatformSprite(g, 50, 400)
g.sprites.append(platform_1)
g.sprites.append(platform_2)
g.sprites.append(platform_3)
g.sprites.append(platform_4)
g.sprites.append(platform_5)
g.sprites.append(platform_6)
g.sprites.append(platform_7)
g.sprites.append(platform_8)
g.sprites.append(platform_9)
for i in range(1):
    i = RandomMovingPlatformSprite(g)
    g.sprites.append(i)
door = DoorSprite(g, 10, 10)
g.sprites.append(door)
sf = StickFigureSprite(g)
g.sprites.append(sf)
g.mainloop()
