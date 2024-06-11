from http.client import HTTPException
from typing import List

from fastapi import APIRouter
from pony.orm import db_session, select


from Classes.MyModels import PositionCreate, PositionRead
from Classes.ORM_classes import Position

router_position = APIRouter()
# CRUD operations for Position
@router_position.post("/positions/", response_model=PositionRead)
@db_session
def create_position(position: PositionCreate):
    new_position = Position(name=position.name, group=position.group)
    return PositionRead(position_id=new_position.position_id, name=new_position.name, group=new_position.group)


@router_position.get("/positions/", response_model=List[PositionRead])
@db_session
def read_positions():
    positions = select(p for p in Position)[:]
    return [PositionRead(position_id=p.position_id, name=p.name, group=p.group) for p in positions]


@router_position.get("/positions/{position_id}", response_model=PositionRead)
@db_session
def read_position(position_id: int):
    position = Position.get(position_id=position_id)
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    return PositionRead(position_id=position.position_id, name=position.name, group=position.group)


@router_position.put("/positions/{position_id}", response_model=PositionRead)
@db_session
def update_position(position_id: int, position: PositionCreate):
    p = Position.get(position_id=position_id)
    if not p:
        raise HTTPException(status_code=404, detail="Position not found")
    p.name = position.name
    p.group = position.group
    return PositionRead(position_id=p.position_id, name=p.name, group=p.group)


@router_position.delete("/positions/{position_id}", response_model=PositionRead)
@db_session
def delete_position(position_id: int):
    p = Position.get(position_id=position_id)
    if not p:
        raise HTTPException(status_code=404, detail="Position not found")
    p.delete()
    return PositionRead(position_id=p.position_id, name=p.name, group=p.group)
