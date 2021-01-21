#  Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(first, second, third):

    numbers = [first, second, third]
    total = []
    max_num_1 = max(numbers)
    total.append(max_num_1)
    numbers.remove(max_num_1)
    max_num_2 = max(numbers)
    total.append(max_num_2)
    print(sum(total))

print(my_func(int(input(f"Введите первое число: ")), int(input(f"Введите второе число: ")), int(input(f"Введите третье число: "))))