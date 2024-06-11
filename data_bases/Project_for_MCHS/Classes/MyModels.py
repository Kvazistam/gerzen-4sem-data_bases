from datetime import date

from pydantic import BaseModel


# Определяем модели для ответа

class PositionCreate(BaseModel):
    name: str
    group: str = None


class PositionRead(BaseModel):
    position_id: int
    name: str
    group: str = None


class RankCreate(BaseModel):
    name: str


class RankRead(BaseModel):
    rank_id: int
    name: str


class EmployeeCreate(BaseModel):
    last_name: str
    first_name: str
    patronymic: str
    date_of_birth: date
    position_id: int
    rank_id: int


class EmployeeRead(BaseModel):
    employee_id: int
    last_name: str
    first_name: str
    patronymic: str
    date_of_birth: date
    position_id: int
    rank_id: int


class AttestationCreate(BaseModel):
    employee_id: int
    RPE_permission: bool
    RPE_permission_deny_reason: str = None
    test_date: date
    permission_order_date: date
    permission_order_number: int
    date: date


class AttestationRead(BaseModel):
    attestation_id: int
    employee_id: int
    RPE_permission: bool
    RPE_permission_deny_reason: str = None
    test_date: date
    permission_order_date: date
    permission_order_number: int
    date: date


class ExerciseTypeCreate(BaseModel):
    name: str


class ExerciseTypeRead(BaseModel):
    Exercise_type_id: int
    name: str


class ExerciseCreate(BaseModel):
    Exercise_type_id: int
    date: date
    address: str
    RFE_type: str = None


class ExerciseRead(BaseModel):
    Exercise_id: int
    Exercise_type_id: int
    date: date
    address: str
    RFE_type: str = None


class EmployeeExerciseCreate(BaseModel):
    exercise_id: int
    employee_id: int


class EmployeeExerciseRead(BaseModel):
    id: int
    exercise_id: int
    employee_id: int


class ReportCreate(BaseModel):
    exercise_id: int
    start_date: date
    finish_date: date
    count_plan: int
    count_actual: int
    count_reason: str
    comment: str = None


class ReportRead(BaseModel):
    Report_id: int
    exercise_id: int
    start_date: date
    finish_date: date
    count_plan: int
    count_actual: int
    count_reason: str
    comment: str = None
