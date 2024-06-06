# Лабораторная работа 7 (2024)

# CRUD - Create Read Update Delete

# con = sqlite3.connect("data.sqlite3")

import sqlite3
import time
import datetime


class MyCounter():
    def __init__(self):
        self.counter = 0

    def reset(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1


class Mydata(dict):
    def __init__(self, id=None, value=None, curent_date= datetime.datetime.now()):
        super().__init__()
        self["id"] = id
        self["value"] = value
        self["date"] = curent_date


def connect_to_db(path_to_db: str) -> sqlite3.Connection:
    print('Подключение к БД')
    # предусмотреть обработку исключения, связанного с
    # sqlite3.Error
    try:
        conn = sqlite3.connect(path_to_db)
        return conn
    except sqlite3.Error as e:
        print(e)


def db_table_create(conn: sqlite3.Connection, query):
    cur = conn.cursor()
    tbl_create = cur.execute(query)
    conn.commit()


def create_data(conn: sqlite3.Connection, data: Mydata):
    # TODO Использовать https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries

    cur = conn.cursor()

    cur.execute("INSERT INTO counter VALUES(:id, :value, :date)", data)

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
    value = int(input("Введите value"))
    date = datetime.datetime.now()
    mydata = Mydata(id, value, date)
    return mydata


def get_params_for_search():
    pass
    # сформировать параметры для параметризации выборки из БД по полям таблицы counter


def main():
    conn = connect_to_db("")
    counter = MyCounter()
    counter.increment()

    # user_input

    db_table_create(
        conn,
        """CREATE TABLE counter (id INT, value INT, created DATETIME);""")

    create_data(conn, Mydata(counter.counter, 1))
    counter.increment()
    create_data(conn,
                Mydata(counter.counter, 2, '2024-04-04 15:54:21'))
    counter.increment()
    create_data(conn,
                Mydata(counter.counter, 1, '2024-04-04 13:30:00'))
    counter.increment()
    read_data(conn, "SELECT * FROM counter;")
    input("Pause. Press Enter for continue ")
    cur_dt = datetime.datetime.now()
    update_data(conn,
                f"UPDATE counter SET created = '{cur_dt}' WHERE id == 1; ")

    read_data(conn, "SELECT * FROM counter;")
    input("Pause. Press Enter for continue ")

    delete_data(conn, "DELETE FROM counter WHERE id == 1;")
    read_data(conn, "SELECT * FROM counter;")
    input("Pause. Press Enter for exit ")


if __name__ == '__main__':
    main()
