import inspect


def task_number(task):  # функция l_number получает номер строки, откуда была вызвана,
    # Получаем информацию о текущем вызове
    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno  # Получаем номер строки
    return f"Задача № {task}, Строка № {line_number} -  "


print(task_number(1))


def smash(words):  # Функция smash принимает на вход список слов (words).
    return " ".join(words)  # Метод ' '.join(words) объединяет слова в строку, добавляя пробел между каждым словом.


words = ['hello', 'world', 'this', 'is', 'great']
sentence = smash(words)
print(task_number(1), sentence)

print(task_number(2))


def make_negative(number):
    pass
    if number <= 0:
        return number
    else:
        return -1 * number


print(task_number(2), make_negative(42))

print(task_number(3))


def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(task_number(3), even_or_odd(35))

print(task_number(4))


def past(h, m, s):
    # Проверка входных данных
    if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
        raise ValueError("Некорректное время: часы (0-23), минуты (0-59), секунды (0-59).")

    # Преобразование времени в миллисекунды
    milliseconds = (h * 3600 + m * 60 + s) * 1000
    return milliseconds


print(task_number(4), past(0, 1, 1))

print(task_number(5))


def fake_bin(number):
    # Преобразуем число в строку, чтобы проработать каждую цифру
    return ''.join('1' if int(digit) >= 5 else '0' for digit in str(number))


print(task_number(5), fake_bin(3482675))  # Для 3482675 результат будет "0001101"

print(task_number(6))


def zero_fuel(distance_to_pump, mpg, fuel_left):
    # Вычисляем максимальное расстояние, которое можно проехать
    max_distance = mpg * fuel_left
    # Проверяем, достаточно ли топлива
    return max_distance >= distance_to_pump


# Пример использования
distance_to_pump = 50  # Расстояние до заправки
miles_per_gallon = 25  # Расход топлива
fuel_remaining = 2  # Остаток топлива
print(task_number(6), zero_fuel(distance_to_pump, miles_per_gallon, fuel_remaining))  # Вывод: True

print(task_number(7))


def reverse_seq(n):
    if n <= 0:
        return []
    return list(range(n, 0, -1))  # Функция range возвращает объект типа range, list преобразует range в список


print(task_number(7), reverse_seq(5))

'''
Чтобы проверить, является ли объект генератором, можно использовать модуль inspect
range — это не генератор, а отдельный тип данных.
range возвращает объект типа range, который эффективно представляет последовательность чисел.
range похож на генераторы в плане ленивых вычислений, но отличается типом и возможностью повторного использования. 
В отличие от генераторов, объекты типа `range` обеспечивают доступ к элементам последовательности по индексу и могут 
использоваться в срезах
'''
import inspect

r = range(5)
g = (x for x in range(5))

print(inspect.isgenerator(r))  # False
print(inspect.isgenerator(g))  # True

print(task_number(8))


def dna_to_rna(dna):
    """
    Преобразует строку ДНК в РНК, заменяя все символы 'T' на 'U'.

    :param dna: Строка ДНК, состоящая из символов 'A', 'C', 'G', 'T'.
    :type dna: str
    :return: Строка РНК, где 'T' заменены на 'U'.
    :rtype: str
    """
    return dna.replace('T', 'U')


# Примеры использования
print(task_number(8), dna_to_rna("GCAT"))  # Вывод: "GCAU"
print(dna_to_rna("ATCG"))  # Вывод: "AUCG"
print(dna_to_rna("TTTT"))  # Вывод: "UUUU"

print(task_number(9))


def greet(name):
    # Good Luck (like you need it)
    return (f"Hello, {name} how are doing today?")


print(task_number(9), greet("Joy"))

print(task_number(10))


def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m


print(task_number(10), paperwork(5, -5))

print(task_number(11))


def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += int(p0 * (percent / 100)) + aug
        years += 1
    return years


print(task_number(11), nb_year(1000, 2, 50, 1200))

print(task_number(12))
import string


# def print_english_alphabet():
#     print(string.ascii_lowercase)  # Для строчных букв
#     print(string.ascii_uppercase)  # Для прописных букв
#
#
# print_english_alphabet()


def print_e(start, end):
    alphabet = string.ascii_lowercase  # Создаем список из букв английского алфавита
    start_index = alphabet.index(start)  # Находим индексы начальной и конечной букв
    end_index = alphabet.index(end) + 1  # +1, чтобы включить конечную букву
    work_colors = alphabet[start_index:end_index]  # Выводим указанный диапазон
    return work_colors


print(task_number(12), print_e('a', 'm'), "  - Получение части алфавита от a до m в нижней раскладке")


def printer_error(s, start='a', stop='m'):
    alphabet = string.ascii_lowercase  # Создаем список из букв английского алфавита
    work_colors = set(alphabet[alphabet.index(start):alphabet.index(stop) + 1])  # Определяем указанный диапазон
    error_count = sum(char for char in s if char not in work_colors)  # Считаем количество ошибок (Для каждого символа
    # проверяется, есть ли он в `work_colors`. Если нет, то генерируется 1.)
    return f"{error_count}/{len(s)}"  # Возвращаем строку с количеством ошибок и длиной строки


print(task_number(12), printer_error("aaabbbbhaijjjm"))


# def printer_error(s):
#     # Определяем допустимые цвета
#     valid_colors = set("abcdefghijklm")
#     # Считаем количество ошибок
#     error_count = sum(1 for char in s if char not in valid_colors)
#     # Возвращаем строку с количеством ошибок и длиной строки
#     return f"{error_count}/{len(s)}"

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))


print(task_number(12), printer_error("aaabbbbhaijjjm"))

s = "taatbbbthaitjjjm"
q = [x for x in s if x not in "abcdefghijklm"]  # Генератор списка: [x for x in s if x not in "abcdefghijklm"]`
# проходит  по каждому символу `x` в строке `s` и проверяет, находится ли он вне диапазона символов от `a` до `m`.
# Условие `if x not in "abcdefghijklm"`: Если символ `x` не входит в строку `"abcdefghijklm"`, он  добавляется в
# список `q`.
print(task_number(12), q)


def converter(mpg):
    imperial_gallon = 4.54609188
    mile = 1.609344
    kpl_base = imperial_gallon / mile
    return round(mpg * kpl_base, 2)


def solution(string):
    string_back = string[len(string)::-1]
    return string_back


print(task_number(13), solution('world'))


def solution(string):
    return string[::-1]


print(task_number(14), solution('world'))
