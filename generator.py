import inspect


def l_number():  # функция l_number получает номер строки, откуда была вызвана,
    # Получаем информацию о текущем вызове
    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno  # Получаем номер строки
    return f"Строка № {line_number} -  "


'''
Чтобы проверить, является ли объект генератором, можно использовать модуль inspect
range — это не генератор, а отдельный тип данных.
range возвращает объект типа range, который эффективно представляет последовательность чисел.
range похож на генераторы в плане ленивых вычислений, но отличается типом и возможностью повторного использования. 
В отличие от генераторов, объекты типа `range` обеспечивают доступ к элементам последовательности по индексу и могут 
использоваться в срезах
'''
print(l_number())
r = range(5)
g = (x for x in range(5))
print(l_number(), list(r))  # фыpываем функцию frame.f_lineno и получаем номер строки перед выводом списка r
print(l_number(), list(g))

print(l_number(), inspect.isgenerator(r))  # False
print(l_number(), inspect.isgenerator(g))  # True

summ = 0
for i in range(5):
    summ += i
print(l_number(), f"В цикле for: {summ}")

summ = sum(i for i in range(5))
print(l_number(), f"В генераторном выражении: {summ}")


def nested_generator():
    for v in range(3):
        yield (j for j in range(v))


'''Объяснение вывода:
Первая итерация (v = 0):
Внутренний генератор: range(0) → пустая последовательность.
Результат: [].
Вторая итерация (v = 1):
Внутренний генератор: range(1) → [0].
Результат: [0].
Третья итерация (v = 2):
Внутренний генератор: range(2) → [0, 1].
Результат: [0, 1].'''

for inside_gen in nested_generator():
    print(l_number(), list(inside_gen))


def nested_generator():
    for v in range(3):
        yield (j for j in range(v))


for inside_gen in nested_generator():
    print(l_number(), list(inside_gen))




