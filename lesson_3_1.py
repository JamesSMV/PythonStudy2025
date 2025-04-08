from my_functions import l_number

# def l_number():  # функция l_number получает номер строки, откуда была вызвана,
#     # Получаем информацию о текущем вызове
#     frame = inspect.currentframe().f_back
#     line_number = frame.f_lineno  # Получаем номер строки
#     return f"Строка № {line_number} -  "
line_num = l_number  # присваивание функции l_number переменной line_number для последующег применения
print(type(line_num))

print(line_num())  # вызываем функцию l_number через переменную line_number
data = ("error", 404)
match data:
    case ("error", code):
        print(f"Ошибка: {code}")
    case ("success", code):
        print(f"Успех: {code}")
    case _:
        print("Неизвестный статус")

# month = int(input(f"{l_number()}Введите номер месяца"))
# match month:
#     case 1 | 2 | 3:
#         print("Зима")
#     case 4 | 5 | 6:
#         print("Весна")
#     case 7 | 8 | 9:
#         print("Лето")
#     case 10 | 11 | 12:
#         print("Осень")

s = 1 | 2 | 3
print(l_number(), s)

point = [1, 1]
match point:
    case (x, y) if x > 0 and y > 0:
        print("Точка в первом квадранте")
    case (x, y) if x < 0 and y > 0:
        print("Точка во втором квадранте")
    case _:
        print("Точка в другом квадранте или на оси")
print(f"\n{l_number()}\n")

word = "abcd"
for i in word:
    for j in range(3):
        print(i, end="-")
        print(j, end=" ")
    print()

result = ""  # Переменная для хранения результата
for i in word:
    for j in range(3):
        result += f"{i}-{j} "  # Добавляем строку к результату
    result += "  "  # можно вставить \n

# Вывод результата в консоль
print(l_number(), result)
print(type(result))

word = "abcd"
result = []
for i in word:
    for j in range(3):
        result.append(i)  # Добавляем строку непосредственно в список
        result.append(j)
print(l_number(), result)

result = []
result1 = ()
for i in word:
    for j in range(3):
        result1 = (i, j)  # создаем кортеж из пары i, j
        result.append(result1)
print(l_number(), result)

result = set()  # создание пустого множества
for i in word:
    for j in range(3):
        result.add(f"{i}{j}")
print(l_number(), result)
print(f"\n{l_number()}\n")

width = 5  # Ширина поля для каждого элемента
rows = 3
cols = 4
matrix_list = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)  # Заполняем элементы, можно использовать любую логику
    matrix_list.append(row)
    print(*(f"{x:{width}}" for x in row))
print(l_number(), matrix_list)

print(f"{(l_number())}  matrix_list[1][0] = {matrix_list[1][0]}")

for row in matrix_list:
    print()
    print(*row)  # *row  распаковывает список row в отдельные аргументы print()

for row in matrix_list:
    print(*(f"{x:{width}}" for x in row))

string1 = "forma"
string2 = "format"
string3 = string1
string3
print(l_number(), string1 == "forma", id(string1))
print(l_number(), string1 == string2, id(string2))
print(l_number(), string1 is string3, type(string3), id(string3))
