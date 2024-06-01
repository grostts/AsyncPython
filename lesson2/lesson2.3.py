# # Чтение файла
# with open('file.txt', 'r') as f:
#     data = f.read()
#
# # Запись в файл
# with open('file.txt', 'w') as f:
#     f.write('Hello, World!')



# import requests
#
# # Отправка GET запроса
# response = requests.get('http://www.python.org')
#
# # Отправка POST запроса
# response = requests.post('http://www.python.org', data={'key':'value'})



# # Чтение ввода с клавиатуры
# name = input('Введите ваше имя: ')
#
# # Вывод информации на экран
# print(f'Привет, {name}!')



# import os
#
# # Получение списка файлов в директории
# files = os.listdir('/path/to/directory')
#
# # Запуск системной команды
# os.system('ls -l')



# import sqlite3
#
# # Подключение к базе данных
# conn = sqlite3.connect('example.db')
#
# # Создание курсора
# c = conn.cursor()
#
# # Выполнение SQL-запроса
# c.execute("SELECT * FROM stocks WHERE symbol = 'RHAT'")



# import serial
#
# # Открытие последовательного порта
# ser = serial.Serial('/dev/ttyUSB0')
#
# # Чтение данных из порта
# data = ser.read(100)



# from selenium import webdriver
#
# # Открытие веб-браузера
# driver = webdriver.Firefox()
#
# # Переход на веб-сайт
# driver.get('http://www.python.org')



# # Арифметические операции
# result = (3 + 4) * 5 / 2
#
# # Логические операции
# is_true = (5 > 3) and (2 < 4)



# # Цикл for
# for i in range(10):
#     print(i)
#
# # Цикл while
# i = 0
# while i < 10:
#     print(i)
#     i += 1



# # Условные операторы
# x = 10
# if x > 5:
#     print('x больше 5')
# elif x < 5:
#     print('x меньше 5')
# else:
#     print('x равно 5')



# # Определение функции
# def square(x):
#     return x ** 2
#
# # Вызов функции
# result = square(5)



# # Сортировка списка
# numbers = [5, 2, 3, 1, 4]
# numbers.sort()
#
# # Поиск в списке
# index = numbers.index(3)



# from PIL import Image
#
# # Открытие изображения
# img = Image.open('image.jpg')
#
# # Применение фильтра
# img = img.filter(ImageFilter.BLUR)
#
# # Сохранение изображения
# img.save('blurred_image.jpg')



# from sklearn.ensemble import RandomForestClassifier
# from sklearn.datasets import load_iris
#
# # Загрузка данных
# iris = load_iris()
# X, y = iris.data, iris.target
#
# # Обучение модели
# clf = RandomForestClassifier()
# clf.fit(X, y)



# import numpy as np
#
# # Создание массива
# x = np.array([1, 2, 3, 4, 5])
#
# # Вычисление синуса для каждого элемента массива
# y = np.sin(x)



# from cryptography.fernet import Fernet
#
# # Генерация ключа
# key = Fernet.generate_key()
#
# # Создание объекта шифрования
# cipher = Fernet(key)
#
# # Шифрование сообщения
# message = b"Hello, World!"
# encrypted_message = cipher.encrypt(message)