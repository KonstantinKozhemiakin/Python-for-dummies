print('''
1. Прямоугольник
Создайте новый холст с помощью функции Pen модуля turtle и изобразите на нем 
прямоугольник.
''')
import tkinter
import turtle

turtle.Pen()
t = turtle.Pen()
t.forward(100)
t.left(90)
t.forward(50)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)

print('''
2. Треугольник
Создайте новый холст и нарисуйте на нем треугольник. Разворачивая черепашку, 
сверяйтесь с изображением окружности и градусов поворота 
''')
t.reset()
t.forward(50)
t.left(120)
t.forward(50)
t.left(120)
t.forward(50)

print('''
3. Рамка без углов
Напишите программу, которая рисует четыре линии, как на этом изображении
(размер «квадрата» неважен, только форма):
''')
t.reset()
t.forward(50)
t.up()
t.right(45)
t.forward(10)
t.down()
t.right(45)
t.forward(50)
t.up()
t.right(45)
t.forward(10)
t.down()
t.right(45)
t.forward(50)
t.up()
t.right(45)
t.forward(10)
t.down()
t.right(45)
t.forward(50)
