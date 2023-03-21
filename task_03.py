print('''
  Создайте две переменные: пусть одна хранит ваше имя, а другая фамилию. 
  Теперь с помощью строки с метками %s напечатайте приветствие 
  вроде такого: «Привет, Брандо Икетт!»
  ''')
my_name = 'Kostyantin'
my_surname = 'Kozhemiakin'
greatings = 'Hy, %s %s!'
print(greatings % (my_name, my_surname))
