# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, но с прописной первой буквой.

word = (input(f"Введите слово из маленьких латинских букв: "))

def int_func():
    return(str.capitalize(word))

print(int_func())



# Второй вариант.

word = (input(f"Введите слово из маленьких латинских букв: "))

def int_func(word):
    return word.title()

print(int_func(word))




