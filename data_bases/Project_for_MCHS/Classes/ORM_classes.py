from datetime import date

from pony.orm import PrimaryKey, Required, Optional, Set

from Classes.Enums import RPE, group
from data_base_property import db


class Position(db.Entity):
    position_id = PrimaryKey(int, auto=True)
    name = Required(str, 45, sql_type="VARCHAR(45)")
    group = Required(str)
    employees = Set('Employee')


class Rank(db.Entity):
    rank_id = PrimaryKey(int, auto=True)
    name = Optional(str, 45, sql_type="VARCHAR(45)")
    employees = Set('Employee')


class Employee(db.Entity):
    employee_id = PrimaryKey(int, auto=True)
    last_name = Required(str, 45, sql_type="VARCHAR(45)")
    first_name = Required(str, 45, sql_type="VARCHAR(45)")
    patronymic = Optional(str, 45, sql_type="VARCHAR(45)")
    date_of_birth = Required(date, sql_type="DATE")
    position_id = Required(Position)
    rank_id = Required(Rank, sql_type="INT")
    exercises = Set('EmployeeExercise')
    attestations = Set('Attestation')


class Attestation(db.Entity):
    attestation_id = PrimaryKey(int, auto=True)
    employee_id = Required(Employee, sql_type="INT")
    PRE_permission = Required(int, sql_type="TINYINT")
    PRE_permission_deny_reason = Optional(str, 45, sql_type="VARCHAR(45)")
    test_date = Required(date, sql_type="DATE")
    permission_order_date = Required(date, sql_type="DATE")
    permission_order_number = Required(int, sql_type="INT")
    date = Required(date, sql_type="DATE")


class Exercise_type(db.Entity):
    exercise_type_id = PrimaryKey(int, auto=True)
    name = Required(str, 45, sql_type="VARCHAR(45)")
    exercises = Set('Exercise')


class Exercise(db.Entity):
    exercise_id = PrimaryKey(int, auto=True)
    exercise_type_id = Required(Exercise_type, sql_type="INT")
    date = Required(date, sql_type="DATE")
    address = Required(str, 45, sql_type="VARCHAR(45)")
    RPE_type = Required(str)
    employees = Set('EmployeeExercise')
    reports = Set('Report')


class EmployeeExercise(db.Entity):
    exercise_id = Required(Exercise, sql_type="INT")
    employee_id = Required(Employee, sql_type="INT")



class Report(db.Entity):
    report_id = PrimaryKey(int, auto=True)
    exercise = Required(Exercise)
    start_date = Required(date, sql_type="DATE")
    finish_date = Optional(date, sql_type="DATE")
    count_plan = Required(int, sql_type="SMALLINT")
    count_acctual = Optional(int, sql_type="SMALLINT")
    count_reason = Optional(str, 45, sql_type="VARCHAR(45)")
    comment = Optional(str, sql_type='TEXT')
