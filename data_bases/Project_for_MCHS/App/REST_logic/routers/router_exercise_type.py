from typing import List

from fastapi import APIRouter
from pony.orm import db_session

from App.REST_logic.CRUD.CRUD_exercise_type import create_exercise_type, read_exercise_types, read_exercise_type, \
    update_exercise_type, delete_exercise_type
from Classes.MyModels import ExerciseTypeRead, ExerciseTypeCreate

router_exercise_type = APIRouter()


# CRUD operations for ExerciseType

@router_exercise_type.post("/exercise_types/", response_model=ExerciseTypeRead)
def create_exercise_type_requests(exercise_type: ExerciseTypeCreate):
    return create_exercise_type(exercise_type)


@router_exercise_type.get("/exercise_types/", response_model=List[ExerciseTypeRead])
@db_session
def read_exercise_types_requests():
    return read_exercise_types()


@router_exercise_type.get("/exercise_types/{exercise_type_id}", response_model=ExerciseTypeRead)
def read_exercise_type_requests(exercise_type_id: int):
    return read_exercise_type(exercise_type_id)


@router_exercise_type.put("/exercise_types/{exercise_type_id}", response_model=ExerciseTypeRead)
def update_exercise_type_requests(exercise_type_id: int, exercise_type: ExerciseTypeCreate):
    return update_exercise_type(exercise_type_id, exercise_type)


@router_exercise_type.delete("/exercise_types/{exercise_type_id}", response_model=ExerciseTypeRead)
def delete_exercise_type_requests(exercise_type_id: int):
    return delete_exercise_type(exercise_type_id)
