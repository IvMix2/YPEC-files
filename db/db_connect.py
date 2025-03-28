import psycopg2
from db.config import host, user, password, db_name

def SQLquery(query, params=None): #Функция отправки запроса к базе денных
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        ) #Подключение базы данных
        connection.autocommit = True
        with connection.cursor() as cursor: #Отправка запроса
            if params: #С параметрами
                cursor.execute(query, params)
            else: #Без параметров
                cursor.execute(query)

            return cursor.fetchall() #Возвращение результата запроса

    except Exception as _ex: #Обработка ошибки
        print(_ex)
    finally:
        if connection:
            connection.close() #Закрытие соединения с базой данных