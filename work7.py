# Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.

word = (input(f"Введите слова через пробел: "))

def int_func(word):
    return word.title()

print(int_func(word))

# Или такой варинат.

def int_func():
    word = input(f"Введите слова через пробел: ")
    print(word.title())
    return
int_func()

#Какой вариант более правильный или не принципиально?