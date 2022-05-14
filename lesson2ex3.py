import math

x = int(input('Введите число: '))

reverse = ""


def add_last_digit(x):
  global reverse
  last_digit = x % 10
  reverse = reverse + str(last_digit)

add_last_digit(x)

while x >= 10:
  x = math.floor(x / 10)
  add_last_digit(x)

print('Обратное:', int(reverse))