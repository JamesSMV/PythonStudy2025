import time
import sys

for i in range(3, 0, -1):
    sys.stdout.write(f'\r{i}')  # Перезаписываем строку
    sys.stdout.flush()  # Обеспечиваем немедленный вывод
    time.sleep(0.5)  # Задержка на 1 секунду
sys.stdout.write('\rСтарт')  # Выводим "Старт"
sys.stdout.flush()

print()


def print_with_delay(text, delay=0.1):
    """
    Выводит текст на печать с задержкой между символами.

    :param text: Текст для вывода.
    :type text: str
    :param delay: Задержка между символами в секундах.
    :type delay: float
    """
    for char in text:
        print(char, end='', flush=True)  # Выводим символ без перевода строки
        time.sleep(delay)  # Задержка
    print()  # Переход на новую строку после завершения


# time.sleep(delay): Приостанавливает выполнение программы на указанное количество секунд.
# print(char, end='', flush=True):
# end='' — предотвращает переход на новую строку после каждого символа.
# flush=True — сразу выводит символ на экран, не буферизируя вывод.


# Пример использования
print_with_delay("Привет", delay=0.5)

# Виды вывода следующей строки при печати, по умолчанию \n
print("H", end='_')
time.sleep(1)
print("i", end='*****')
print("!", end='')
