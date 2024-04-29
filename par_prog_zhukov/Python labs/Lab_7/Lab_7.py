# Лабораторная работа 6 (2024)

# CRUD - Create Read Update Delete

# con = sqlite3.connect("data.sqlite3")

import sqlite3


def connect_to_db(path_to_db: str) -> sqlite3.Connection:

    print('Подключение к БД')
    # предусмотреть обработку исключения, связанного с
    # sqlite3.Error
    conn = sqlite3.connect(path_to_db)

    return conn


def db_table_create(conn: sqlite3.Connection, query):
    cur = conn.cursor()
    tbl_create = cur.execute(query)
    conn.commit()


def create_data(conn: sqlite3.Connection, query):
    # TODO Использовать https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries

    cur = conn.cursor()

    cur.execute(query)

    conn.commit()


def read_data(conn: sqlite3.Connection, query):
    read_result = conn.execute(query)

    for _row in read_result:
        print(_row)


def update_data(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()


def delete_data(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()


def user_input():

    id = int(input("Введите id"))
    # value = int(input("Введите id"))
    # value = int(input("Введите id"))

    # created = datetime or pendulum
    # d - сформировать объект для параметризованной вставки в БД и выполнения запросов для SELECT
    return d


def get_params_for_search():
    pass
    # сформировать параметры для параметризации выборки из БД по полям таблицы counter


def main():

    conn = connect_to_db(":memory:")

    # user_input

    db_table_create(
        conn,
        """CREATE TABLE counter (id INT, value INT, created DATETIME);""")

    create_data(conn,
                "INSERT INTO counter VALUES (1, 1, '2024-30-03 15:37:21');")
    create_data(conn,
                "INSERT INTO counter VALUES (2, 2, '2024-04-04 15:54:21');")

    create_data(conn,
                "INSERT INTO counter VALUES (3, 1, '2024-04-04 13:30:00');")

    read_data(conn, "SELECT * FROM counter;")
    input("Pause. Press Enter for continue ")
    cur_dt = '2024-30-03 15:00:00'  # TODO: С использованием библиотеки datetime / pendulum вставлять текущее время
    update_data(conn,
                f"UPDATE counter SET created = '{cur_dt}' WHERE id == 1; ")

    read_data(conn, "SELECT * FROM counter;")
    input("Pause. Press Enter for continue ")

    delete_data(conn, "DELETE FROM counter WHERE id == 1;")
    read_data(conn, "SELECT * FROM counter;")
    input("Pause. Press Enter for exit ")


if __name__ == '__main__':
    main()

