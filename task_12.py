print('''
#1. Заполните экран треугольниками
Напишите программу, которая с помощью tkinter заполняет экран треугольниками. 
Затем модифицируйте код, чтобы треугольники были раскрашены (заполнены) 
различными цветами.
''')

from tkinter import *
import time
import random

my_width = 400
my_height = 400
my_count = 5

tk = Tk()
canvas = Canvas(tk, width=my_width, height=my_height)
canvas.pack()


def random_triangle(height, width):
    x1 = random.randrange(height)
    x2 = random.randrange(width)
    x3 = random.randrange(height)
    x4 = random.randrange(width)
    x5 = random.randrange(height)
    x6 = random.randrange(width)
    de = ("%02x" % random.randint(0, 255))
    re = ("%02x" % random.randint(0, 255))
    we = ("%02x" % random.randint(0, 255))
    ge = "#"
    rand_color = ge + de + re + we
    canvas.create_polygon(x1, x2, x3, x4, x5, x6, fill=rand_color, outline=rand_color)


def many_random_triangle(height, width, count):
    for i in range(0, count):
        random_triangle(height, width)


many_random_triangle(my_height, my_width, my_count)
tk.mainloop()

print('''
#2. Движущийся треугольник
Доработайте код движущегося треугольника (см. «Создание простой 
анимации» на стр. 181), чтобы треугольник двигался вправо, вниз, влево 
и вверх, вернувшись в итоге в первоначальную позицию.
''')

my_width = 400
my_height = 400
my_count = 60
my_timesleep = 0.05
tk = Tk()
canvas = Canvas(tk, width=my_width, height=my_height)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
for x in range(0, my_count):
    canvas.move(1, 5, 0)
    tk.update()
    time.sleep(my_timesleep)
for x in range(0, my_count):
    canvas.move(1, 0, 5)
    tk.update()
    time.sleep(my_timesleep)
for x in range(0, my_count):
    canvas.move(1, -5, 0)
    tk.update()
    time.sleep(my_timesleep)
for x in range(0, my_count):
    canvas.move(1, 0, -5)
    tk.update()
    time.sleep(my_timesleep)
tk.mainloop()

print('''
#3. Движущаяся фотография
С помощью tkinter отобразите на экране свою фотографию. Не забывайте, 
что изображение должно быть в формате GIF! А теперь сделайте 
так, чтобы фотография перемещалась по экрану.
''')

my_width = 1000
my_height = 1000
tk = Tk()
canvas = Canvas(tk, width=my_width, height=my_height)
canvas.pack()
my_image = PhotoImage(file='test.gif')
canvas.create_image(0, 0, anchor=NW, image=my_image)


def move_photo(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)


canvas.bind_all('<KeyPress-Up>', move_photo)
canvas.bind_all('<KeyPress-Down>', move_photo)
canvas.bind_all('<KeyPress-Left>', move_photo)
canvas.bind_all('<KeyPress-Right>', move_photo)
tk.mainloop()
