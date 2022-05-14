import math

x = int(input('Введите число: '))

odd = 0
even = 0


def last_odd_or_even(x):
  global odd, even
  last_digit = x % 10
  if last_digit % 2 == 0:
    even += 1
  else:
    odd += 1


last_odd_or_even(x)

while x >= 10:
  x = math.floor(x / 10)
  last_odd_or_even(x)

print('Нечётных:', odd)
print('Чётных:', even)