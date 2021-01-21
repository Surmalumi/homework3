# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
def sum():
    result = 0
    while True:
        numbers = input(f"Введите несколько чисел с пробелами или знак = для выхода: ").split()
        for i in numbers:
            try:
                if i == "=":
                    print(f' Сумма чисел будет равна {result}.')
                    return
                else:
                   result += int(i)
            except ValueError:
                print('Введите еще числа или знак = для выхода')
        print(f'Сумма чисел равна {result}')
print(sum())


