import copy
import inspect


def l_number():  # функция l_number получает номер строки, откуда была вызвана,
    # Получаем информацию о текущем вызове
    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno  # Получаем номер строки
    return f"Строка № {line_number} -  "


print()
print("множество")
a = {1, 3, 7, 9}
print(l_number(), type(a))
print(l_number(), f"вывод a {a}")
b = a
print(l_number(), f"вывод b {b}")
b.remove(3)
b.add(300)
b.add(500)
print(l_number(), f"вывод b {b}")
print(l_number(), f"вывод a {a}")
print(l_number(), type(a))
print()

print("immutable")
a = (2, 4, 6, 8)
print(l_number(), f"вывод a {a}")
b = a
print(l_number(), f"вывод b {b}")
b = (300)
print(l_number(), f"вывод b {b}")
print(l_number(), f"вывод a {a}")
print()

a = "2, 4, 6, 8"
print(l_number(), f"вывод a {a}")
b = a
print(l_number(), f"вывод b {b}")
b = "300"
print(l_number(), f"вывод b {b}")
print(l_number(), f"вывод a {a}")
# c = a.index(1, 3)
print()

print("mutable")
a = [2, 4, 6, 8, [40, 50, 60]]
print(l_number(), f"вывод типа a: {type(a)}")
print(l_number(), f"вывод названия типа a: {type(a).__name__}")
print(l_number(), f"вывод a {a}")
a.insert(0, 4444)
print(l_number(), f"вывод a {a}")
b = a
c = a.copy()
d = copy.deepcopy(a)
d[5][2] = 777
c.append(700)
print(l_number(), f"итог b = a {b}")
print(l_number(), f"итог a.copy c {c}")
c[5][1] = 65
print(l_number(), f"вывод a {a}")
print(l_number(), f"итог b = a {b}")
print(l_number(), f"итог a.copy c{c}")
print(l_number(), f"итог d = copy.deepcopy(a) {d}")
b[1] = 500
b.append(400)
print(l_number(), f"вывод b {b}")
print(l_number(), f"вывод a {a}")

string1 = "forma"
string2 = "format"
string3 = string1

print(l_number(), string1 == "forma", id(string1))
print(l_number(), string1 == string2, id(string2))
print(l_number(), string1 is string3, type(string3), id(string3))

string4 = "gyUgEkwY yDsrS7gUn"
sorted_string1 = "".join(sorted(string4))  # Сортировка символов строки. Функция sorted() возвращает новый
# отсортированный список символов, а метод join() объединяет эти символы обратно в строку:
print(l_number(), sorted_string1)

# при сравнении строк в отсортированной таблице, можно использовать параметр `key` в функции `sorted()`,
# который позволяет указать функцию для преобразования строк перед сортировкой.  В данном случае можно задать функцию
# `str.lower`, чтобы преобразовать все строки в нижний регистр перед сравнением
sorted_string2 = "".join(sorted(string4, key=str.lower))
print(l_number(), sorted_string2)

print(l_number(), sorted_string1 == "gyUgEkwY yDsrS7gUn")
print(l_number(), sorted_string1 == sorted_string2, id(sorted_string1))
print(l_number(), sorted_string1 is sorted_string2, id(sorted_string2), type(sorted_string2))
print(l_number(), string4 == sorted_string1, id(string4))
print(l_number(), string4 is sorted_string1, id(sorted_string1))
print(l_number(), *string4, type(string4))
print(l_number(), "g", "y", "U")
print(l_number(), list(string4))
print(f"{l_number()} вывод среза string4[2:10:2] = {string4[2:10:2]}")
