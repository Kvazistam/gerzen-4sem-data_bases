from fastapi import HTTPException
from pony.orm import db_session, select, commit

from Classes.MyModels import ExerciseTypeRead, ExerciseTypeCreate
from Classes.ORM_classes import Exercise_type


# CRUD operations for ExerciseType


@db_session
def create_exercise_type(exercise_type: ExerciseTypeCreate):
    new_exercise_type = Exercise_type(name=exercise_type.name)
    commit()
    return ExerciseTypeRead(Exercise_type_id=new_exercise_type.Exercise_type_id, name=new_exercise_type.name)



@db_session
def read_exercise_types():
    exercise_types = select(et for et in Exercise_type)[:]
    return [ExerciseTypeRead(Exercise_type_id=et.Exercise_type_id, name=et.name) for et in exercise_types]



@db_session
def read_exercise_type(exercise_type_id: int):
    exercise_type = Exercise_type.get(Exercise_type_id=exercise_type_id)
    if not exercise_type:
        raise HTTPException(status_code=404, detail="ExerciseType not found")
    return ExerciseTypeRead(Exercise_type_id=exercise_type.Exercise_type_id, name=exercise_type.name)


@db_session
def update_exercise_type(exercise_type_id: int, exercise_type: ExerciseTypeCreate):
    et = Exercise_type.get(Exercise_type_id=exercise_type_id)
    if not et:
        raise HTTPException(status_code=404, detail="ExerciseType not found")
    et.name = exercise_type.name
    commit()
    return ExerciseTypeRead(Exercise_type_id=et.Exercise_type_id, name=et.name)


@db_session
def delete_exercise_type(exercise_type_id: int):
    et = Exercise_type.get(Exercise_type_id=exercise_type_id)
    if not et:
        raise HTTPException(status_code=404, detail="ExerciseType not found")
    et.delete()
    return ExerciseTypeRead(Exercise_type_id=et.Exercise_type_id, name=et.name)
