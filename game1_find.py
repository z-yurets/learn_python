import random
tryMe = random.randint(1, 20)
tryIt, minShot, maxShot = 0, 1, 20
for tryIt in range(6):
    shot = int(minShot + (maxShot - minShot)/2)
    print('Ану, ' + str(shot) + '?')
    if shot < tryMe:
        print('Недолёт')
        minShot = shot
    if shot > tryMe:
        print('Переплюнув')
        maxShot = shot
    if shot == tryMe:
        print('Опача, вгадав')
        break
print('Ты потратил ' + str(tryIt + 1) + ' попыток')