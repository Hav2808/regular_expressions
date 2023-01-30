import re
from pprint import pprint
import csv

filename = "phonebook_raw.csv"

PHONE_PATTERN = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_SUB = r'+7(\2)\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ

def main(contact_list: list):
    new_list = list()
    for i in contact_list:
        line = ' '.join(i[:3]).split(' ')
        result = [line[0], line[1], line[2], i[3], i[4],
                  re.sub(PHONE_PATTERN, PHONE_SUB, i[5]),
                  i[6]]
        new_list.append(result)
    return union(new_list)


def union(elements: list):
    """функция которая убирает одинаковые и пустые запятые и дублирование записей"""
    for element in elements:
        first_name = element[0]
        last_name = element[1]
        for new_element in elements:
            new_first_name = new_element[0]
            new_last_name = new_element[1]
            if first_name == new_first_name and last_name == new_last_name:
                if element[2] == "":
                    element[2] = new_element[2]
                if element[3] == "":
                    element[3] = new_element[3]
                if element[4] == "":
                    element[4] = new_element[4]
                if element[5] == "":
                    element[5] = new_element[5]
                if element[6] == "":
                    element[6] = new_element[6]

    result_list = list()
    #pprint(elements)
    # print("*"*100)
    for i in elements:
        if i not in result_list:
            result_list.append(i)
    #pprint(result_list)
    return result_list



# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(main(contacts_list))


# Домашнее задание к лекции 5.«Regular expressions»
# Иногда при знакомстве мы записываем контакты в адресную книгу кое-как с мыслью, что "когда-нибудь потом все обязательно поправим". Копируем данные из интернета или из смски. Добавляем людей в разных мессенджерах. В результате получается адресная книга, в которой совершенно невозможно кого-то нормально найти: мешает множество дублей и разная запись одних и тех же имен.
#
# Кейс основан на реальных данных из https://www.nalog.ru/opendata/, https://www.minfin.ru/ru/opendata/
#
# Ваша задача: починить адресную книгу, используя регулярные выражения.
# Структура данных будет всегда:
# lastname,firstname,surname,organization,position,phone,email
# Предполагается, что телефон и e-mail у человека может быть только один.
# Необходимо:
#
# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
# привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;
# объединить все дублирующиеся записи о человеке в одну.
#
# from pprint import pprint
# # читаем адресную книгу в формате CSV в список contacts_list
# import csv
# with open("phonebook_raw.csv") as f:
#   rows = csv.reader(f, delimiter=",")
#   contacts_list = list(rows)
# pprint(contacts_list)
#
# # TODO 1: выполните пункты 1-3 ДЗ
# # ваш код
#
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)