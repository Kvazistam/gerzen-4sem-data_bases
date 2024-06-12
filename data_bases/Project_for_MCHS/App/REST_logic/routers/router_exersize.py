from fastapi import HTTPException, APIRouter
from pony.orm import db_session, select
from typing import List

from App.REST_logic.CRUD.CRUD_exercise import create_exercise, read_exercises, read_exercise, update_exercise, \
    delete_exercise
from Classes.MyModels import ExerciseRead, ExerciseCreate
from Classes.ORM_classes import Exercise_type, Exercise

router_exercise = APIRouter()


# CRUD operations for Exercise

@router_exercise.post("/exercises/", response_model=ExerciseRead)
def create_exercise_request(exercise: ExerciseCreate):
    return create_exercise(exercise)


@router_exercise.get("/exercises/", response_model=List[ExerciseRead])
def read_exercises_request():
    return read_exercises()


@router_exercise.get("/exercises/{exercise_id}", response_model=ExerciseRead)
def read_exercise_request(exercise_id: int):
    return read_exercise(exercise_id)


@router_exercise.put("/exercises/{exercise_id}", response_model=ExerciseRead)
def update_exercise_request(exercise_id: int, exercise: ExerciseCreate):
    return update_exercise(exercise_id, exercise)


@router_exercise.delete("/exercises/{exercise_id}", response_model=ExerciseRead)
def delete_exercise_request(exercise_id: int):
    return delete_exercise(exercise_id)
