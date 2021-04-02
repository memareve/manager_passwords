import random
import time
import csv
"""Менеджер паролей"""

def pass_generation(length):
    digits = '1234567890'
    leters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leters_2 = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%^&*()-+'
    password = ''
    var = [digits, leters, leters_2, symbols]
    if length < 12:
        print('Ошибка! Пароль должен иметь не менее 12 символов')
        return pass_generation(int(input('Введите длину пароля > 12 симв.: ')))
    else:
        password += random.choice(digits)
        password += random.choice(leters)
        password += random.choice(leters_2)
        password += random.choice(symbols)
        while len(password) < length:
            password += random.choice(var[random.randint(0, 3)])
        return password


def save(array):
    with open('data.csv', 'w') as file:
        datawrite = csv.writer(file)
        for info in array:
            datawrite.writerow(info)
    print('Все данные сохранены!')
    exit()


def boot_screen():
    print('''█───█─███─█──█─███──███──█─█─█─███─████
██─██─█───█──█─█────█─█──█████─█───█──█
█─█─█─███─████─███──█─█───███──███─████
█───█─█───█──█─█───█████─█████─█───█
█───█─███─█──█─███─█───█─█─█─█─███─█
────────────────────────────────
████─████─████─████───██─███─█──█
█──█─█──█─█──█─█──█──█─█─█───█──█
█──█─████─████─█──█─█──█─███─█─██
█──█─█──█─█────█──█─█──█─█───██─█
█──█─█──█─█────████─█──█─███─█──█''')
    print()
    time.sleep(2)
    a = []
    b = []
    with open('data.csv', 'r') as file:
        for line in file:
            cleanedline = line.strip()
            if cleanedline:
                b.append(cleanedline)
                a.append(b[0].split(','))
                b = []
    actions(a)


def actions(array):
    # print(array) - для удобства просмотра работы программы
    print()
    try:
        print('Действия:')
        a = int(input('1. Добавить данные входа\n2. Удалить данные входа\n3. Изменить данные входа\n'
                      '4. Посмотреть данные входа\n5. Список сайтов в базе данных для входа\n'
                      '6. Выход из программы и сохранение изменений\n'))
        if a == 1:
            print()
            add(array)
        elif a == 2:
            print()
            delete(array)
        elif a == 3:
            print()
            change(array)
        elif a == 4:
            print()
            look(array)
        elif a == 5:
            print()
            look_sites(array)
        elif a == 6:
            print('''████─████─████─████──████──██─██─███
█────█──█─█──█─█──██─█──██──███──█
█─██─█──█─█──█─█──██─████────█───███
█──█─█──█─█──█─█──██─█──██───█───█
████─████─████─████──████────█───███
───────────────────────────────────''')
            save(array)
        else:
            actions(array)
    except ValueError:
        actions(array)


def add(array):
    c = []
    print('____________________________')
    print('Введите название сайта:')
    name = input()
    for i in range(len(array)):
        if array[i][0] == name:
            print('Такой сайт уже существует.')
            add(array)
    print('Введите логин/email:')
    login = input()
    try:
        ans = int(input('1. Ввести свой пароль\n2. Сгенерировать надежный пароль\n'))
        if ans == 1:
            password = input('Введите пароль:\n')
        elif ans == 2:
            password = pass_generation(int(input('Введите длину пароля > 12 симв.: ')))
            print('Сгенерирован пароль:', password)
        else:
            print('Ошибка ввода, попробуйте еще раз.')
            print()
            add(array)
    except ValueError:
        print('Ошибка ввода, попробуйте еще раз.')
        print()
        add(array)
    c.extend([name, login, password])
    array.append(c)
    print('Данные входа успешно добавлены')
    actions(array)


def delete(array):
    print('____________________________')
    print('Введите название сайта для удаления данных входа:')
    name = input()
    for n, el in enumerate(array):
        if el[0] == name:
            del array[n]
            actions(array)
    print('Такой сайт не существует.')
    delete(array)


def change(array):
    print('____________________________')
    print('Введите название сайта для изменения данных входа:')
    name = input()
    for i in range(len(array)):
        if array[i][0] == name:
            break
    else:
        print('Такой сайт не существует.')
        change(array)
    print('Что вы хотите изменить?\n1. Логин\n2. Пароль')
    try:
        ans = int(input())
        if ans == 1:
            for i in range(len(array)):
                if array[i][0] == name:
                    print('Введите новый логин для сайта', name)
                    array[i][1] = input()
                    print('Логин для сайта', name, 'изменен на:', array[i][1])
                    actions(array)
        elif ans == 2:
            for i in range(len(array)):
                if array[i][0] == name:
                    print('Введите новый пароль для сайта', name)
                    array[i][2] = input()
                    print('Пароль для сайта', name, 'изменен на:', array[i][2])
                    actions(array)
        else:
            print('Ошибка ввода, попробуйте еще раз.')
            print()
            change(array)
    except ValueError:
        print('Ошибка ввода, попробуйте еще раз.')
        print()
        change(array)


def look(array):
    print('____________________________')
    print('Введите название сайта для просмотра данных входа:')
    name = input()
    for i in range(len(array)):
        if array[i][0] == name:
            print('Данные для входа на сайт ', name, ':', sep='')
            print('Логин:', array[i][1])
            print('Пароль:', array[i][2])
            time.sleep(3)
            actions(array)
    else:
        print('Такой сайт не существует.')
        change(array)


def look_sites(array):
    print('____________________________')
    print('Список сайтов в базе данных для входа:')
    for i in range(len(array)):
        print(array[i][0])
    time.sleep(2)
    actions(array)


boot_screen()
