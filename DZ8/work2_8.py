# Задание 2: Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке


my_list = ['May spring\n', 'June\n', 'Jule\n']
with open("test_2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("test_2.txt") as file_obj:
    lines = 0
    words = 0
    for line in file_obj:
        lines += line.count("\n")
        words = len(line.split())
        print(f"{words} слов в строке")
    print(f"Количество строк {lines}")
