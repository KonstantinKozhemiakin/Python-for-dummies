print('''
#1. Жирафий танец
Добавьте в класс Giraffes функции, при вызове которых жираф переставлял бы 
правую или левую ногу вперед либо назад. 
Назвать их можно так: left_foot_forward, left_foot_back, right_foot_forward
и right_foot_back. 
Теперь создайте функцию dance, которая научит Реджинальда танцевать 
(вызывая четыре только что созданные функции для передвижения ног). 
В результате должен получиться несложный танец:
>>> reginald = Giraffes()
>>> reginald.dance()
левая нога впереди
левая нога сзади
правая нога впереди
правая нога сзади
левая нога сзади
правая нога сзади
правая нога впереди
левая нога впереди
''')


class Things:
    pass


class Animate(Things):
    def breathe(self):
        print('дышит')

    def move(self):
        print('двигается')

    def eat_food(self):
        print('ест')


class Animals(Animate):
    pass


class Mammals(Animals):
    def feed_young_with_milk(self):
        print('кормит детенышей молоком')


class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('ест листья')

    def left_foot_forward(self):
        print('левая нога впереди')

    def left_foot_back(self):
        print('левая нога сзади')

    def right_foot_forward(self):
        print('правая нога впереди')

    def right_foot_back(self):
        print('правая нога сзади')

    def dance(self):
        self.left_foot_forward()
        self.left_foot_back()
        self.right_foot_forward()
        self.right_foot_back()
        self.left_foot_back()
        self.right_foot_back()
        self.right_foot_forward()
        self.left_foot_forward()


reginald = Giraffes()
reginald.dance()

print('''
#2. Черепашьи вилы
При помощи четырех черепашек (объектов класса Pen) изобразите вилы, 
как на этой картинке (длину линий выберите на свой вкус).
''')
import tkinter
import turtle

turtle.Pen()
t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()
t1.forward(200)
t2.forward(220)
t3.forward(220)
t4.forward(200)
t1.left(90)
t2.left(90)
t3.right(90)
t4.right(90)
t1.forward(40)
t2.forward(20)
t3.forward(20)
t4.forward(40)
t4.left(90)
t3.left(90)
t2.right(90)
t1.right(90)
t1.forward(60)
t2.forward(20)
t3.forward(20)
t4.forward(60)
