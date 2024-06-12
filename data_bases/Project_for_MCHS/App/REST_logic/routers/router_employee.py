from typing import List

from fastapi import APIRouter

from App.REST_logic.CRUD.CRUD_employee import create_employee, read_employees, read_employee, update_employee, \
    delete_employee
from Classes.MyModels import EmployeeCreate, EmployeeRead

router_employee = APIRouter()


# CRUD operations for Employee
@router_employee.post("/employees/", response_model=EmployeeRead)
def create_employee_request(employee: EmployeeCreate):
    return create_employee(employee)


@router_employee.get("/employees/", response_model=List[EmployeeRead])
def read_employees_request():
    return read_employees()


@router_employee.get("/employees/{employee_id}", response_model=EmployeeRead)
def read_employee_request(employee_id: int):
    return read_employee(employee_id)


@router_employee.put("/employees/{employee_id}", response_model=EmployeeRead)
def update_employee_request(employee_id: int, employee: EmployeeCreate):
    return update_employee(employee_id, employee)


@router_employee.delete("/employees/{employee_id}", response_model=EmployeeRead)
def delete_employee_request(employee_id: int):
    return delete_employee(employee_id)
