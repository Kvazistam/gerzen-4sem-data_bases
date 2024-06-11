from fastapi import HTTPException, APIRouter
from pony.orm import db_session, select
from typing import List

from Classes.MyModels import ExerciseRead, ExerciseCreate
from Classes.ORM_classes import Exercise_type, Exercise


router_exercise = APIRouter()

# CRUD operations for Exercise

@router_exercise.post("/exercises/", response_model=ExerciseRead)
@db_session
def create_exercise(exercise: ExerciseCreate):
    exercise_type = Exercise_type.get(Exercise_type_id=exercise.Exercise_type_id)
    if not exercise_type:
        raise HTTPException(status_code=400, detail="Invalid ExerciseType ID")
    new_exercise = Exercise(
        Exercise_type=exercise_type,
        date=exercise.date,
        address=exercise.address,
        RFE_type=exercise.RFE_type
    )
    return ExerciseRead(
        Exercise_id=new_exercise.Exercise_id,
        Exercise_type_id=new_exercise.Exercise_type.Exercise_type_id,
        date=new_exercise.date,
        address=new_exercise.address,
        RFE_type=new_exercise.RFE_type
    )


@router_exercise.get("/exercises/", response_model=List[ExerciseRead])
@db_session
def read_exercises():
    exercises = select(e for e in Exercise)[:]
    return [ExerciseRead(
        Exercise_id=e.Exercise_id,
        Exercise_type_id=e.Exercise_type.Exercise_type_id,
        date=e.date,
        address=e.address,
        RFE_type=e.RFE_type
    ) for e in exercises]


@router_exercise.get("/exercises/{exercise_id}", response_model=ExerciseRead)
@db_session
def read_exercise(exercise_id: int):
    exercise = Exercise.get(Exercise_id=exercise_id)
    if not exercise:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return ExerciseRead(
        Exercise_id=exercise.Exercise_id,
        Exercise_type_id=exercise.Exercise_type.Exercise_type_id,
        date=exercise.date,
        address=exercise.address,
        RFE_type=exercise.RFE_type
    )


@router_exercise.put("/exercises/{exercise_id}", response_model=ExerciseRead)
@db_session
def update_exercise(exercise_id: int, exercise: ExerciseCreate):
    ex = Exercise.get(Exercise_id=exercise_id)
    if not ex:
        raise HTTPException(status_code=404, detail="Exercise not found")
    exercise_type = Exercise_type.get(Exercise_type_id=exercise.Exercise_type_id)
    if not exercise_type:
        raise HTTPException(status_code=400, detail="Invalid ExerciseType ID")
    ex.Exercise_type = exercise_type
    ex.date = exercise.date
    ex.address = exercise.address
    ex.RFE_type = exercise.RFE_type
    return ExerciseRead(
        Exercise_id=ex.Exercise_id,
        Exercise_type_id=ex.Exercise_type.Exercise_type_id,
        date=ex.date,
        address=ex.address,
        RFE_type=ex.RFE_type
    )


@router_exercise.delete("/exercises/{exercise_id}", response_model=ExerciseRead)
@db_session
def delete_exercise(exercise_id: int):
    ex = Exercise.get(Exercise_id=exercise_id)
    if not ex:
        raise HTTPException(status_code=404, detail="Exercise not found")
    ex.delete()
    return ExerciseRead(
        Exercise_id=ex.Exercise_id,
        Exercise_type_id=ex.Exercise_type.Exercise_type_id,
        date=ex.date,
        address=ex.address,
        RFE_type=ex.RFE_type
    )
