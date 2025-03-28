import json
from deepseek.prompt_generator import generate_prompt
from deepseek.deepseek import deepseek_query
from db.query_functions import get_column_names
from db.query_functions import insert_data
from db.query_functions import is_have_data, delete_data

def get_int_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Неккоректное значение!")

while True:
    table_name = input("Название таблицы: ")
    column_names = get_column_names(table_name)
    if column_names == -1:
        while column_names == -1:
            table_name = input("Неккоректное название таблицы!\nНазвание таблицы: ")
            column_names = get_column_names(table_name)

    if is_have_data(table_name):
        delete_data_or_no = input("Удалить текущие данные (y/n)? ")
        while not((delete_data_or_no == "y") or (delete_data_or_no == "n")):
            delete_data_or_no = input("Неправильный ввод! Повторите попытку: ")
        if delete_data_or_no == "y":
            delete_data(table_name)


    rows = get_int_input("Количество записей: ")
    min_rep = get_int_input("Минимальное количество повторений в записях: ")
    max_rep = get_int_input("Максимальное количество повторений в записях: ")

    prompt = generate_prompt(
        rows=rows,
        column_names=column_names,
        min_num_of_repetitions=min_rep,
        max_num_of_repetitions=max_rep,
    )
    print(prompt)
    try:
        r = deepseek_query(prompt)
        json_data = ""
        try:
            json_data = json.loads(r)
        except Exception as e:
            print("Ошибка генерации, аварийное завершение!")
            last_brace_index = r.rfind("}")
            if last_brace_index != -1:
                er_data = r[:last_brace_index+1]
                er_data += "]"
                json_data = json.loads(er_data)
                print(json_data)
        insert_data(table_name, json_data, column_names)
    except Exception as ex:
        print('\nНепредвиденная ощибка! :\n', ex)
