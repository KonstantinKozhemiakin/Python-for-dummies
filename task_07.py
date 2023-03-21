print('''
1. Функция лунного веса
Одним из заданий к главе 6 было создание цикла for для 
расчета вашего веса на Луне в течение 15 лет. Этот цикл 
можно оформить в виде функции. Создайте функцию, которая принимает начальный вес 
и величину, на которую вес увеличивается каждый год. Вызывать эту новую функцию 
нужно будет примерно так: moon_weight(30, 0.25)
''')
luna_coeficient = 0.165
period = 15


def moon_weight(weight, plus_weight):
    for i in range(0, period):
        luna_weight = weight * luna_coeficient
        print(luna_weight)
        weight = weight + plus_weight


moon_weight(30, 0.25)

print('''
2. Функция лунного веса и количество лет
Измените функцию из предыдущего задания так, чтобы с ее помощью 
можно было рассчитывать вес для разного количества лет, например 5 
или 20 лет. Пусть эта функция принимает три аргумента: начальный вес, 
прибавку веса в год и количество лет: moon_weight(90, 0.25, 5)
''')
luna_coeficient = 0.165


def moon_weight(weight, plus_weight, period):
    for i in range(0, period):
        luna_weight = weight * luna_coeficient
        print(luna_weight)
        weight = weight + plus_weight


moon_weight(60, 0.25, 5)

print('''
#3. Программа для лунного веса
Вместо простой функции, принимающей значения в виде аргументов, 
можно написать мини-программу, которая будет запрашивать эти значения с помощью 
sys.stdin.readline(). Тогда этой функции вообще не нужны аргументы: moon_weight()
''')
import sys

luna_coeficient = 0.165


def moon_weight():
    # weight = int(sys.stdin.readline())
    weight = int(input('Какой ваш вес сейчас?'))
    plus_weight = int(input('На сколько ежегодно будет увеличиваться вес?'))
    period = int(input('Сколько лет рассчитать?'))
    for i in range(0, period):
        luna_weight = weight * luna_coeficient
        print(luna_weight)
        weight = weight + plus_weight


moon_weight()
