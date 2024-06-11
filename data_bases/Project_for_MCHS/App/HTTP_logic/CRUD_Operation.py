from typing import List

from fastapi import HTTPException, APIRouter
from pony.orm import db_session, select

from Classes.MyModels import PositionRead, PositionCreate
from Classes.ORM_classes import Position

router_operation = APIRouter()
# CRUD operations for Position
@router_operation.post("/positions/", response_model=PositionRead)
@db_session
def create_position(position: PositionCreate):
    new_position = Position(name=position.name, group=position.group)
    return PositionRead(position_id=new_position.position_id, name=new_position.name, group=new_position.group)


@router_operation.get("/positions/", response_model=List[PositionRead])
@db_session
def read_positions():
    positions = select(p for p in Position)[:]
    return [PositionRead(position_id=p.position_id, name=p.name, group=p.group) for p in positions]


@router_operation.get("/positions/{position_id}", response_model=PositionRead)
@db_session
def read_position(position_id: int):
    position = Position.get(position_id=position_id)
    if not position:
        raise HTTPException(status_code=404, detail="Position not found")
    return PositionRead(position_id=position.position_id, name=position.name, group=position.group)


@router_operation.put("/positions/{position_id}", response_model=PositionRead)
@db_session
def update_position(position_id: int, position: PositionCreate):
    pos = Position.get(position_id=position_id)
    if not pos:
        raise HTTPException(status_code=404, detail="Position not found")
    pos.name = position.name
    pos.group = position.group
    return PositionRead(position_id=pos.position_id, name=pos.name, group=pos.group)


@router_operation.delete("/positions/{position_id}", response_model=PositionRead)
@db_session
def delete_position(position_id: int):
    pos = Position.get(position_id=position_id)
    if not pos:
        raise HTTPException(status_code=404, detail="Position not found")
    pos.delete()
    return PositionRead(position_id=pos.position_id, name=pos.name, group=pos.group)
