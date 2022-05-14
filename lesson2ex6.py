import random

mysterious_number = random.randrange(0, 100)

for i in range(10, 0, -1):
  x = int(input('Ваш предположение: '))
  if x == mysterious_number:
    print('Правильно!')
    exit()
  elif x < mysterious_number:
    print('Слишком маленькое число')
  else:
    print('Слишком большое число')

print('Вы проиграли, правильный ответ: ', mysterious_number)