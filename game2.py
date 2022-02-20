from random import random


import random
import time
def ride():
    for a in range(random.randint(1, 20)):
        print('Тыгыдык ', end='')
        # time.sleep(2)
    if a <= 9:
        print('\nНедалеко оказалось')
    elif a >= 15:
        print('\nДолго ехал')
    else:
        print('\nНормально покатался')

ride()
