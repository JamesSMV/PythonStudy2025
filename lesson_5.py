from my_functions import l_number


class User:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__money = 0  # Приватный атрибут ```__money```доступен только внутри класса (недоступен даже в
        # наследнике), только  set или get
        User.add_count()

    def great(self):
        print(f"Hi, {self.name}!")

    def add_money(self, n):
        self.__money += n

    @classmethod
    def add_count(cls):  # метод класса, действует для всех экземпляров класса, нужен при повторяющихся действиях
        cls.count += 1  # добавляет значение при создании нового объекта

    @staticmethod  # метод класса без указания ```self```` или ```cls```
    def is_valid_age(age):
        return age > 18

    # Выводит строку вместо ```<__main__.User object at 0x7f1c3932c110>``` (вывод информации пользователю, логирование)
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r})"

    # Выводит строку вместо ```<__main__.User object at 0x7f1c3932c110>``` (отладка, вывод в консоли Python,
    # представление в контейнерах)
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def get_all(self):
        return f"name - {self.name}, age - {self.age}"

    def get_money(self):
        return f"money - {self.__money}"

    def set_money(self, money):
        self.__money = money

    def set_name(self, new_name):
        self.name = new_name


user1 = User("James", 22)
print(l_number(), User.count, user1.name)
user2 = User("Yohan", 35)
print(l_number(), User.count, user1.name, user1.age)
print(l_number(), User.count, user2.name, user2.age)
print(l_number(), User.is_valid_age(12))
print(l_number(), user1.is_valid_age(user1.age))
print(l_number("При наличии обоих методов __str__ и __repr__ выводит как __str__"), user1)
print(l_number("Используется метод __str__"), str(user1))
print(l_number("Используется метод __repr__"), repr(user1))

print(l_number("get метод"), user1.get_all())
user1.name = 333
print(l_number("get метод"), user1.get_all())
user1.set_name("Eugene")
print(l_number("get метод"), user1.get_all())

print(l_number("приватный атрибут __money"), user1.get_money())
user1.set_money(10)
user1.money = 900  # Не меняет значение
user1.__money = 900  # Не меняет значение
print(l_number("приватный атрибут __money"), user1.get_money())






