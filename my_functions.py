import inspect


def l_number(coment=" "):  # функция l_number получает номер строки, откуда была вызвана,
    # Получаем информацию о текущем вызове

    frame = inspect.currentframe().f_back
    line_number = frame.f_lineno  # Получаем номер строки
    return f"Строка № {line_number}     ... {coment} ...    "


if __name__ == "__main__":
    l_number()
