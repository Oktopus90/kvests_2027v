import csv
import datetime
import os
import shutil
from zipfile import ZipFile

import wget

BASE_DIR = os.getcwd()


def clear_works():
    """Очистка работ."""
    try:
        shutil.rmtree('works')
    except KeyError as error:
        print('Удаление не получилось', error)


def unzip_student(name, zip_file):
    with ZipFile(zip_file) as myzip:
        myzip.extractall(f'works/{name}')


def download_student_work(name, url):
    try:
        download_url = f'{url}/archive/heads/main.zip'
        time_now = datetime.datetime.now().strftime("%Y%m%d %H_%M")
        name_dir = f'works/{name}_{time_now}'
        os.makedirs(f'works/{name_dir}')
        save_url = f'works/{name_dir}'
        zip_file = wget.download(download_url, save_url)
        unzip_student(name_dir, zip_file)
        os.remove(f'{zip_file}')
    except KeyError as error:
        print(">>>>", "Скачивание файла прервалось с ошикой\n", error)


clear_works()

with open('student.csv') as students:
    read_student = csv.reader(students, delimiter=',')
    for student in read_student:
        print(">>>>>student", student)
        if student[1].startswith('https://github.com/'):
            name, url = student[0], student[1]
            #print(name, url)
            try:
                download_student_work(name, url)
            except KeyError as error:
                print(">>>>Ошибка", error)
