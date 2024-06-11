from typing import List

from fastapi import HTTPException, APIRouter
from pony.orm import db_session, select

from Classes.MyModels import EmployeeCreate, EmployeeRead
from Classes.ORM_classes import Position, Rank, Employee

router_employee = APIRouter()
# CRUD operations for Employee
@router_employee.post("/employees/", response_model=EmployeeRead)
@db_session
def create_employee(employee: EmployeeCreate):
    position = Position.get(position_id=employee.position_id)
    rank = Rank.get(rank_id=employee.rank_id)
    if not position or not rank:
        raise HTTPException(status_code=400, detail="Invalid position or rank ID")
    new_employee = Employee(
        last_name=employee.last_name,
        first_name=employee.first_name,
        patronymic=employee.patronymic,
        date_of_birth=employee.date_of_birth,
        position=position,
        rank=rank
    )
    return EmployeeRead(
        employee_id=new_employee.employee_id,
        last_name=new_employee.last_name,
        first_name=new_employee.first_name,
        patronymic=new_employee.patronymic,
        date_of_birth=new_employee.date_of_birth,
        position_id=new_employee.position.position_id,
        rank_id=new_employee.rank.rank_id
    )


@router_employee.get("/employees/", response_model=List[EmployeeRead])
@db_session
def read_employees():
    employees = select(e for e in Employee)[:]
    return [EmployeeRead(
        employee_id=e.employee_id,
        last_name=e.last_name,
        first_name=e.first_name,
        patronymic=e.patronymic,
        date_of_birth=e.date_of_birth,
        position_id=e.position.position_id,
        rank_id=e.rank.rank_id
    ) for e in employees]


@router_employee.get("/employees/{employee_id}", response_model=EmployeeRead)
@db_session
def read_employee(employee_id: int):
    employee = Employee.get(employee_id=employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return EmployeeRead(
        employee_id=employee.employee_id,
        last_name=employee.last_name,
        first_name=employee.first_name,
        patronymic=employee.patronymic,
        date_of_birth=employee.date_of_birth,
        position_id=employee.position.position_id,
        rank_id=employee.rank.rank_id
    )


@router_employee.put("/employees/{employee_id}", response_model=EmployeeRead)
@db_session
def update_employee(employee_id: int, employee: EmployeeCreate):
    emp = Employee.get(employee_id=employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    position = Position.get(position_id=employee.position_id)
    rank = Rank.get(rank_id=employee.rank_id)
    if not position or not rank:
        raise HTTPException(status_code=400, detail="Invalid position or rank ID")
    emp.last_name = employee.last_name
    emp.first_name = employee.first_name
    emp.patronymic = employee.patronymic
    emp.date_of_birth = employee.date_of_birth
    emp.position = position
    emp.rank = rank
    return EmployeeRead(
        employee_id=emp.employee_id,
        last_name=emp.last_name,
        first_name=emp.first_name,
        patronymic=emp.patronymic,
        date_of_birth=emp.date_of_birth,
        position_id=emp.position.position_id,
        rank_id=emp.rank.rank_id
    )


@router_employee.delete("/employees/{employee_id}", response_model=EmployeeRead)
@db_session
def delete_employee(employee_id: int):
    emp = Employee.get(employee_id=employee_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.delete()
    return EmployeeRead(
        employee_id=emp.employee_id,
        last_name=emp.last_name,
        first_name=emp.first_name,
        patronymic=emp.patronymic,
        date_of_birth=emp.date_of_birth,
        position_id=emp.position.position_id,
        rank_id=emp.rank.rank_id
    )
