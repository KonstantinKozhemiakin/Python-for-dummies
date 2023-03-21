print('''
#1. Что выведет на экран этот код?
''')
import copy


class Car:
    pass


car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)

car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)

print('''
#2. Создайте список ваших любимых вещей, а затем с помощью pickle 
запишите его в файл favorites.dat. Закройте оболочку Python, запустите ее 
снова и напечатайте содержимое вашего списка, загрузив его из файла.
''')

import pickle

faworite_things = ['salo', 'pizza', 'beer']
save_file = open('save.dat', 'wb')
pickle.dump(faworite_things, save_file)
save_file.close()

import pickle

load_file = open('save.dat', 'rb')
load_data = pickle.load(load_file)
load_file.close()
print(load_data)
