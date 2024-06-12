from typing import List

from fastapi import APIRouter
from pony.orm import select

from App.REST_logic.CRUD.CRUD_position import create_position, read_positions, read_position, update_position, \
    delete_position
from Classes.MyModels import PositionCreate, PositionRead
from Classes.ORM_classes import Position

router_position = APIRouter()


# CRUD operations for Position
@router_position.post("/positions/", response_model=PositionRead)
def create_position_request(position: PositionCreate):
    return create_position(position)


@router_position.get("/positions/", response_model=List[PositionRead])
def read_positions_request():
    positions = select(p for p in Position)[:]
    return read_positions()


@router_position.get("/positions/{position_id}", response_model=PositionRead)
def read_position_request(position_id: int):
    return read_position(position_id)


@router_position.put("/positions/{position_id}", response_model=PositionRead)
def update_position_request(position_id: int, position: PositionCreate):
    return update_position(position_id, position)


@router_position.delete("/positions/{position_id}", response_model=PositionRead)
def delete_position_request(position_id: int):
    return delete_position(position_id)
