import requests
import easygui
import os


def recognise_photo():
    url = "http://127.0.0.1:8000/recognise"
    file_path = easygui.fileopenbox(filetypes=["*.docx"])
    # Открываем файл для чтения в бинарном режиме
    with open(file_path, 'rb') as file:
        # Создаем словарь с файлом для параметра 'files'
        files = {'file': file}
        # Делаем POST запрос, передавая 'files'
        response = requests.post(url, files=files)

    # Проверяем статус код ответа
    #response.raise_for_status()
    if response.status_code == 200:
        print("Файл успешно загружен.")
        print(response.json())  # Вывод ответа сервера
    else:
        print(f"Ошибка загрузки файла: {response.status_code}")


def get_file_table(filename):
    url = f"http://localhost:8000/get_file/{filename}"  # Замените на ваш URL
    # Делаем GET запрос
    response = requests.get(url)

    # Проверяем статус код ответа
    if response.status_code == 200:

        # Сохраняем содержимое файла
        with open(f"client_data/{filename}", 'wb') as f:
            f.write(response.content)

        print(f"Файл {filename} успешно скачан.")
    else:
        print(f"Ошибка скачивания файла: {response.status_code}")


def upload_file_table():
    url = "http://127.0.0.1:8000/upload"
    file_path = easygui.fileopenbox(filetypes=["*.docx"])
    # Открываем файл для чтения в бинарном режиме
    with open(file_path, 'rb') as file:
        # Создаем словарь с файлом для параметра 'files'
        files = {'file': file}
        # Делаем POST запрос, передавая 'files'
        response = requests.post(url, files=files)

    if response.status_code == 200:
        print("Файл успешно загружен.")
        print(response.json())  # Вывод ответа сервера
    else:
        print(f"Ошибка загрузки файла: {response.status_code}")


def start_excel():
    os.system('start excel.exe client_data/table.xlsx')
