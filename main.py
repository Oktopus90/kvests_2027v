import wget
import csv
from zipfile import ZipFile
import os
import shutil
import datetime
BASE_DIR = os.getcwd()


def clear_works():
    """Очистка работ."""
    try:
        shutil.rmtree('works')
    except:
        print('Удаление не получилось')


def unzip_student(name, zip_file):
    with ZipFile(zip_file) as myzip:
        myzip.extractall(f'works/{name}')
    


def download_student_work(name, url):
    download_url = f'{url}/archive/heads/main.zip'
    time_now = datetime.datetime.now().strftime("%Y%m%d %H_%M")
    name_dir = f'works/{name}_{time_now}'
    os.makedirs(f'works/{name_dir}')
    save_url = f'works/{name_dir}'
    zip_file = wget.download(download_url, save_url)
    unzip_student(name_dir, zip_file)
    os.remove(f'{zip_file}')

clear_works()

with open('student.csv') as students:
    read_student = csv.reader(students, delimiter=',')
    for name, url in read_student:
        print(name, url)
        download_student_work(name, url)


# students = 
# url = 'https://github.com/denialeksbf1231/thequest/archive/heads/main.zip'
# r = wget.download(url, '.')

