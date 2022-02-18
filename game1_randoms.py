import random
tryMe = random.randint(1, 20)
tryIt = 0
for tryIt in range(6):
    shot = random.randint(1, 20)
    print('Ану, ' + str(shot) + '?')
    if shot < tryMe:
        print('Недолёт')
    if shot > tryMe:
        print('Переплюнув')
    if shot == tryMe:
        print('Опача, вгадав')
        break
print('Ты потратил ' + str(tryIt + 1) + ' попыток')