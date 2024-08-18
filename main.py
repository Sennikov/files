import os
import time
from pprint import pprint




# Задача №1
# Должен получится следующий словарь

# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
def read_cook_book():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')
    cook_book ={}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ingr_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'],ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ingr_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ingr_list
    return cook_book


# Задача №2
# Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить

# На выходе мы должны получить словарь с названием ингредиентов и его количества для блюда. Например, для такого вызова
#
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# Должен быть следующий результат:
#
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'n\"Такого блюда нет в книге!"')

    return ingr_list


# Задача №3
#
# Необходимо объединить их в один по следующим правилам:
#
# 1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
# (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
#
# 2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

# def rewrite_file(path1=None, path2=None, path3=None):
#     if path1 or path2 or path3 is None:
#         path1 = '1.txt'
#         path2 = '2.txt'
#         path3 = '3.txt'
#         os.chdir('sorted')
#         outout_file = "rewrite_file.txt"
#         file1_path = os.path.join(os.getcwd(), path1)
#         file2_path = os.path.join(os.getcwd(), path2)
#         file3_path = os.path.join(os.getcwd(), path3)
#         with open(file1_path, 'r', encoding='utf-8') as f1:
#             file1 = f1.readlines()
#         with open(file2_path, 'r', encoding='utf-8') as f2:
#             file2 = f2.readlines()
#         with open(file3_path, 'r', encoding='utf-8') as f3:
#             file3 = f3.readlines()
#         with open(outout_file, 'w', encoding='utf-8') as f_total:
#
#             if len(file1) < len(file2) and len(file1) < len(file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file2) < len(file1) and len(file2) < len(file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file3) < len(file1) and len(file3) < len(file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
#                     file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#                 f_total.write('\n')
#             elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
#                     file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#                 f_total.write('\n')
#             elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
#                     file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#                 f_total.write('\n')
#             if len(file1) > len(file2) and len(file1) > len(file3):
#                 f_total.write(path1 + '\n')
#                 f_total.write(str(len(file1)) + '\n')
#                 f_total.writelines(file1)
#             elif len(file2) > len(file1) and len(file2) > len(file3):
#                 f_total.write(path2 + '\n')
#                 f_total.write(str(len(file2)) + '\n')
#                 f_total.writelines(file2)
#             elif len(file3) > len(file1) and len(file3) > len(file2):
#                 f_total.write(path3 + '\n')
#                 f_total.write(str(len(file3)) + '\n')
#                 f_total.writelines(file3)
#     else:
#         print('Нет параметров')
#     return


import os
import os.path


def strings_count(file):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(1 for line in f)


base_path = os.getcwd()
location = os.path.abspath('D:/Dev/files/sorted/')
file_for_write = os.path.abspath('D:/Dev/files/sorted/rewrite_file.txt')
full_path = os.path.join(base_path, location)


def rewrite(full_path, file_for_write):
    files = []
    for i in list(os.listdir(full_path)):
        files.append([strings_count(os.path.join(full_path, i)), os.path.join(base_path, location, i), i])
    for file_item in sorted(files):
        opening_files = open(file_for_write, 'a', encoding='utf-8')
        opening_files.write(f'{file_item[2]}\n')
        opening_files.write(f'{file_item[0]}\n')
        with open(file_item[1], 'r', encoding='utf-8') as file:
            counting = 1
            for line in file:
                opening_files.write(f'строка № {counting} в файле {file_item[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


rewrite(full_path, file_for_write)


if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cook_book()
    print('Задание #1')
    time.sleep(1)
    print(cook_book)
    print('Задание #2')
    pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель','Омлет'], person_count=2))

    time.sleep(2)
    print('Задание #3')
    # rewrite_file()

