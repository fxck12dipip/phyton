from os import urandom as _urandom


def random(list):
    random = int(int.from_bytes(_urandom(7), 'big')) >> 5
    maxsize = len(list)
    i = random % maxsize
    return list[i]


def frange(start, stop, jump):
    while start < stop:
        yield start
        start += jump


print('Введите диапазон. Диапазон целых чисел \
(type_range = int start_int end_int jump_int). \
Или диапазон вещественных чисел \
(type_range = float start_float end_float jump_float). \
Или диапазон символов \
(type_range = str tart_str end_str jump_int) ')

type_range, raw_start, raw_end, raw_jump = [
    x for x in input('Введите диапазон: type_range start end jump: ').split()
]

if type_range == 'int':
    start = int(raw_start)
    stop = int(raw_end)
    jump = int(raw_jump)
    list_int = [x for x in range(start, stop + 1, jump)]
    print(list_int)
    print(
        f'Случайное целое число из диапазона {start} - {stop}: \
    {random(list_int)}'
    )

elif type_range == 'float':
    start = float(raw_start)
    stop = float(raw_end)
    jump = float(raw_jump)
    list_float = [x for x in frange(start, stop + jump, jump)]
    print(list_float)
    print(
        f'Случайное вещественное число из диапазона {start} - {stop}: \
    {random(list_float)}'
        )

elif type_range == 'str':
    start = raw_start
    stop = raw_end
    jump = int(raw_jump)
    list_abc = [chr(i) for i in range(ord(start), ord(stop) + 1, jump)]
    print(list_abc)
    print(f'Случайный символ из из диапазона {start} - {stop}: \
    {random(list_abc)}')

else:
    print('Неправильно задан диапазон')