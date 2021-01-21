# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон

def info_person(name, surname, birthday_year, city, email, phone):
    print(name, surname, birthday_year, city, email, phone)

info_person(name= 'Moon', surname='Shine', birthday_year=2050, city='Galaxy', email='name@mail.ru', phone='0123456789')

# Сделала еще через **kwargs:

def info_person(**kwargs):
    return kwargs

print(info_person(name='Moon', surname='Shine',  birthday_year=2050, city='Galaxy', email='name@mail.ru', phone='0123456789'))