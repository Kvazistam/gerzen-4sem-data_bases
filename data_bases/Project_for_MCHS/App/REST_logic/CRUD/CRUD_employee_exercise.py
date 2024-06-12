from fastapi import HTTPException
from pony.orm import db_session, select, commit

from Classes.MyModels import EmployeeExerciseRead, EmployeeExerciseCreate
from Classes.ORM_classes import Exercise, Employee, EmployeeExercise


# CRUD operations for EmployeeExercise

@db_session
def create_employee_exercise(employee_exercise: EmployeeExerciseCreate):
    exercise = Exercise.get(Exercise_id=employee_exercise.exercise_id)
    employee = Employee.get(employee_id=employee_exercise.employee_id)
    if not exercise or not employee:
        raise HTTPException(status_code=400, detail="Invalid Exercise ID or Employee ID")
    new_employee_exercise = EmployeeExercise(exercise=exercise, employee=employee)
    commit()
    return EmployeeExerciseRead(
        id=new_employee_exercise.id,
        exercise_id=new_employee_exercise.exercise.Exercise_id,
        employee_id=new_employee_exercise.employee.employee_id
    )


@db_session
def read_employee_exercises():
    employee_exercises = select(ee for ee in EmployeeExercise)[:]
    return [EmployeeExerciseRead(
        id=ee.id,
        exercise_id=ee.exercise.Exercise_id,
        employee_id=ee.employee.employee_id
    ) for ee in employee_exercises]


@db_session
def read_employee_exercise(employee_exercise_id: int):
    employee_exercise = EmployeeExercise.get(id=employee_exercise_id)
    if not employee_exercise:
        raise HTTPException(status_code=404, detail="EmployeeExercise not found")
    return EmployeeExerciseRead(
        id=employee_exercise.id,
        exercise_id=employee_exercise.exercise.Exercise_id,
        employee_id=employee_exercise.employee.employee_id
    )


@db_session
def update_employee_exercise(employee_exercise_id: int, employee_exercise: EmployeeExerciseCreate):
    ee = EmployeeExercise.get(id=employee_exercise_id)
    if not ee:
        raise HTTPException(status_code=404, detail="EmployeeExercise not found")
    exercise = Exercise.get(Exercise_id=employee_exercise.exercise_id)
    employee = Employee.get(employee_id=employee_exercise.employee_id)
    if not exercise or not employee:
        raise HTTPException(status_code=400, detail="Invalid Exercise ID or Employee ID")
    ee.exercise = exercise
    ee.employee = employee
    commit()
    return EmployeeExerciseRead(
        id=ee.id,
        exercise_id=ee.exercise.Exercise_id,
        employee_id=ee.employee.employee_id
    )


@db_session
def delete_employee_exercise(employee_exercise_id: int):
    ee = EmployeeExercise.get(id=employee_exercise_id)
    if not ee:
        raise HTTPException(status_code=404, detail="EmployeeExercise not found")
    ee.delete()
    return EmployeeExerciseRead(
        id=ee.id,
        exercise_id=ee.exercise.Exercise_id,
        employee_id=ee.employee.employee_id
    )
