# 3)	Задание на закрепление знаний по модулю CSV. Написать скрипт,
# осуществляющий выборку определенных данных из файлов info_1.txt,
# info_2.txt, info_3.txt и формирующий новый «отчетный» файл в
# формате CSV. Для этого:
# a) Создать функцию get_data(), в которой в цикле осуществляется
# перебор файлов с данными, их открытие и считывание данных. В этой
# функции из считанных данных необходимо с помощью регулярных выражений
# извлечь значения параметров «Изготовитель системы»,  «Название ОС»,
# «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например,
# os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
# функции создать главный список для хранения данных отчета — например,
# main_data — и поместить в него названия столбцов отчета в виде списка:
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в
# файл main_data (также для каждого файла);
# b) Создать функцию write_to_csv(), в которую передавать ссылку
# на CSV-файл. В этой функции реализовать получение данных через вызов
# функции get_data(), а также сохранение подготовленных данных
# в соответствующий CSV-файл;
# c) Проверить работу программы через вызов функции write_to_csv()


import csv
import re

def get_data():
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта',
              'Тип системы']]

    for filename in range(1, 4):
        with open(f'info_{filename}.txt', encoding='windows-1251') as f:
            file_data = f.read()

        os_prod = re.findall(r'Изготовитель системы:\s+(.*)\n', file_data)[0]
        os_name = re.findall(r'Название ОС:\s+(.*)\n', file_data)[0]
        os_code = re.findall(r'Код продукта:\s+(.*)\n', file_data)[0]
        os_type = re.findall(r'Тип системы:\s+(.*)\n', file_data)[0]

        os_prod_list.append(os_prod)
        os_name_list.append(os_name)
        os_code_list.append(os_code)
        os_type_list.append(os_type)

        main_data.append([filename, os_prod, os_name, os_code, os_type])
        main_data.append("")
    return main_data

def write_to_csv(csv_file):
    data = get_data()

    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f'Данные сохранены в {csv_file}')

if __name__ == '__main__':
    write_to_csv('data_report.csv')
