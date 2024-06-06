# Лабораторная работа 8 (2024)

# CRUD - Create Read Update Delete


import sqlite3
import datetime
from pony.orm import *
# set_sql_debug(True)


class MyCounter():
    def __init__(self):
        self.counter = 0

    def reset(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1

db = Database()

class Mydata(db.Entity):
    value = Required(int)
    date = Required(str)

@db_session
def connect_to_db(path_to_db: str) -> sqlite3.Connection:
    print('Подключение к БД')
    # предусмотреть обработку исключения, связанного с
    # sqlite3.Error
    try:
        db.bind(provider='sqlite', filename=':memory:', create_db=True)
    except sqlite3.Error as e:
        print(e)


def db_table_create(database):
    database.generate_mapping(create_tables=True)

@db_session
def create_data(data: dict):
    Mydata(value=data['value'], date=data['date'])


@db_session
def read_data():
    Mydata.select()[:].show()

@db_session
def update_data(pid,data: dict):
    p = Mydata[pid]
    if 'value' in data.keys():
        p.value = data['value']
    if 'date' in data.keys():
        p.date = data['date']

@db_session
def delete_data(pid):
    Mydata[pid].delete()

@db_session
def user_input():
    value = int(input("Введите value"))
    date = datetime.datetime.now()
    mydata = Mydata(value, date)


def get_params_for_search():
    pass
    # сформировать параметры для параметризации выборки из БД по полям таблицы counter


def main():
    conn = connect_to_db("")
    counter = MyCounter()
    counter.increment()

    # user_input

    db_table_create(db)

    create_data({'value':1,'date':str(datetime.datetime.now())})
    counter.increment()
    create_data({'value':2,'date':str(datetime.datetime.now())})
    counter.increment()
    create_data({'value':3,'date':str(datetime.datetime.now())})
    counter.increment()
    read_data()
    input("Pause. Press Enter for continue ")
    cur_dt = datetime.datetime.now()
    update_data(1,{'date': str(datetime.datetime.now())})

    read_data()
    input("Pause. Press Enter for continue ")

    delete_data(1)
    read_data()
    input("Pause. Press Enter for exit ")


if __name__ == '__main__':
    main()
