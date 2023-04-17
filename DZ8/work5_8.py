# 4)	Задание на закрепление знаний по модулю json. Есть файл
# orders в формате JSON с информацией о заказах. Написать скрипт,
# автоматизирующий его заполнение данными. Для этого:
# a)	Создать функцию write_order_to_json(), в которую передается 5
# параметров — товар (item), количество (quantity), цена (price),
# покупатель (buyer), дата (date). Функция должна предусматривать
# запись данных в виде словаря в файл orders.json. При записи данных
# указать величину отступа в 4 пробельных символа;
# b)	Проверить работу программы через вызов функции
# write_order_to_json() с передачей в нее значений каждого параметра.


import os
import json

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def write_order_to_json(item, quantity, price, buyer, date):
    filename = os.path.join(CURRENT_DIR, 'orders.json')

    if os.path.exists(filename):
        data = {}

    with open(filename, encoding="utf-8") as my_f:
        data = json.loads(my_f.read())

    data['orders'].append({'item': item, 'quantity': quantity,
                           'price': price, 'buyer': buyer,
                           'date': date})

    with open(filename, "w", encoding="utf-8") as my_f:
        json.dump(data, my_f, indent=4, separators=(',', ': '),
                  ensure_ascii=False)
    print(f'Данные добавлены в {filename}')

if __name__ == '__main__':
    write_order_to_json('Fridge INDESIT RTM 16S', '2',
                        '20000', 'Fedorov', '03.03.2023')
    write_order_to_json('Kettle Scarlett SC-EK27G94', '4',
                        '2000', 'Maksimova', '24.03.2023')
    write_order_to_json('Home Element HE-HP702',
                        '10', '1000', 'Kuzina', '25.03.2023')
