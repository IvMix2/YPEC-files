from db.db_connect import SQLquery
from psycopg2 import extensions
def get_column_names(table_name):
    query = "SELECT column_name FROM information_schema.columns WHERE table_name = %s"
    response = SQLquery(query, params=(table_name,))
    if response == []:
        return -1
    else:
        finaly_response = []
        for i in response:
            finaly_response.append(i[0])
        return finaly_response

def insert_data(table_name, data, columns):
    query = f"INSERT INTO %s ("
    for column in columns:
        query += f"{column}, "
    query = query[:-2]
    query += ") VALUES"
    for row in data:
        query += "("
        for key, value in row.items():
            query += f"'{value}', "
        query = query[:-2]+"), "
    query = query[:-2]

    SQLquery(query, (extensions.AsIs(table_name),))

def delete_data(table_name):
    query = f"DELETE FROM %s"
    SQLquery(query, (extensions.AsIs(table_name),))

def is_have_data(table_name):
    query = "SELECT * FROM %s LIMIT 1"
    response = SQLquery(query, (extensions.AsIs(table_name),))
    if response == []:
        return False
    else:
        return True

