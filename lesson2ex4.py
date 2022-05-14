n = int(input('Введите число: '))

if n == 0:
  print('Sum:', 0)
  exit()


result = 1


for i in range(1, n):
  if i % 2 == 0:
    result += 1 / (2**i)
  else:
    result += 1 / -(2**i)

print('Сумма:', result)