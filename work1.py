# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.

def dev(number_1, number_2):
    try:
        result = number_1 / number_2
        return result
    except ZeroDivisionError:
        return "We can't divide by zero!"

print(dev(int(input(f"Введите целое число: ")), int(input(f"Введите еще одно целое число: "))))
