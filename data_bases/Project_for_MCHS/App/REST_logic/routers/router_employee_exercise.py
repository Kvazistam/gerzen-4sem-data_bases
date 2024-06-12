from typing import List

from fastapi import APIRouter

from App.REST_logic.CRUD.CRUD_employee_exercise import create_employee_exercise, read_employee_exercises, \
    read_employee_exercise, update_employee_exercise, delete_employee_exercise
from Classes.MyModels import EmployeeExerciseRead, EmployeeExerciseCreate

router_employee_exercise = APIRouter()


# CRUD operations for EmployeeExercise

@router_employee_exercise.post("/employee_exercises/", response_model=EmployeeExerciseRead)
def create_employee_exercise_request(employee_exercise: EmployeeExerciseCreate):
    return create_employee_exercise(employee_exercise)


@router_employee_exercise.get("/employee_exercises/", response_model=List[EmployeeExerciseRead])
def read_employee_exercises_request():
    return read_employee_exercises()


@router_employee_exercise.get("/employee_exercises/{employee_exercise_id}", response_model=EmployeeExerciseRead)
def read_employee_exercise_request(employee_exercise_id: int):
    return read_employee_exercise(employee_exercise_id)


@router_employee_exercise.put("/employee_exercises/{employee_exercise_id}", response_model=EmployeeExerciseRead)
def update_employee_exercise_request(employee_exercise_id: int, employee_exercise: EmployeeExerciseCreate):
    return update_employee_exercise(employee_exercise_id, employee_exercise)


@router_employee_exercise.delete("/employee_exercises/{employee_exercise_id}", response_model=EmployeeExerciseRead)
def delete_employee_exercise_request(employee_exercise_id: int):
    return delete_employee_exercise(employee_exercise_id)
