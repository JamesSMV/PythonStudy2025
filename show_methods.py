import textwrap


def print_with_wrap(text, width):
    wrapped_text = textwrap.fill(text, width=width)
    print(wrapped_text)


a = "слово"
print(type(a))
c = dir(a)
print(type(c))
print(f"{c}\n")
b = str(dir(a))
print(type(b))
print(f"{b}\n")
print_with_wrap(b, 120)

max_length = 5
print(f"\n{c[:max_length]}{'...' if len(c) > max_length else ''}")
print(f"\n{b[:max_length]}{'...' if len(b) > max_length else ''}")

help(c)  # Функция help() предоставляет подробную документацию по объекту, включая список методов.
