# Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.

def my_func():
    print(6**(-5))

print(my_func())


def my_func(a=6, n=-5):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n > 0:
        return a * my_func(a, n-1)
    elif n < 0:
       return 1.0 / my_func(a, -n)
    return 1
print(my_func())
