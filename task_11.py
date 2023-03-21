print('''
#1. Рисуем восьмиугольник
Мы уже умеем рисовать звезды, квадраты и прямоугольники. А теперь 
создадим функцию для рисования восьмиугольника.
''')

import tkinter
import turtle

t = turtle.Pen()


def octagon(size, filled):
    if filled == True:
        t.begin_fill()
    for x in range(0, 8):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()


t.color(0.9, 0.75, 0)
octagon(20, True)
t.clear()

print('''
#2. Заполненный восьмиугольник
Измените функцию для рисования восьмиугольника так, чтобы она изображала 
восьмиугольник заполненным. Попробуйте обвести его контур, 
как мы это делали раньше со звездой
''')

t = turtle.Pen()


def octagon(size, filled, contour):
    if filled == True:
        t.begin_fill()
    for x in range(1, 9):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()
    if contour == True:
        t.color(0, 0, 0)
        for x in range(1, 9):
            t.forward(size)
            t.left(45)


t.color(0.9, 0.75, 0)
octagon(20, True, True)
t.clear()

print('''
#3. Еще одна функция для рисования звезд
Создайте функцию для рисования звезд, которая принимает два аргумента: 
размер и количество точек, между которыми проведены линии, 
составляющие фигуру.
''')

t = turtle.Pen()


def draw_star(size, points):
    tipcorner = 5
    cavity = (360 + points * tipcorner) / points
    for x in range(points * 2):
        t.forward(size)
        if x % 2 == 0:
            t.left(180 - tipcorner)
        else:
            t.right(180 - cavity)


draw_star(50, 5)
