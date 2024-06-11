from typing import List

from fastapi import HTTPException, APIRouter
from pony.orm import db_session, select


from Classes.MyModels import RankCreate, RankRead
from Classes.ORM_classes import Rank

router_rank = APIRouter()
# CRUD operations for Rank
@router_rank.post("/ranks/", response_model=RankRead)
@db_session
def create_rank(rank: RankCreate):
    new_rank = Rank(name=rank.name)
    return RankRead(rank_id=new_rank.rank_id, name=new_rank.name)


@router_rank.get("/ranks/", response_model=List[RankRead])
@db_session
def read_ranks():
    ranks = select(r for r in Rank)[:]
    return [RankRead(rank_id=r.rank_id, name=r.name) for r in ranks]


@router_rank.get("/ranks/{rank_id}", response_model=RankRead)
@db_session
def read_rank(rank_id: int):
    rank = Rank.get(rank_id=rank_id)
    if not rank:
        raise HTTPException(status_code=404, detail="Rank not found")
    return RankRead(rank_id=rank.rank_id, name=rank.name)


@router_rank.put("/ranks/{rank_id}", response_model=RankRead)
@db_session
def update_rank(rank_id: int, rank: RankCreate):
    r = Rank.get(rank_id=rank_id)
    if not r:
        raise HTTPException(status_code=404, detail="Rank not found")
    r.name = rank.name
    return RankRead(rank_id=r.rank_id, name=r.name)


@router_rank.delete("/ranks/{rank_id}", response_model=RankRead)
@db_session
def delete_rank(rank_id: int):
    r = Rank.get(rank_id=rank_id)
    if not r:
        raise HTTPException(status_code=404, detail="Rank not found")
    r.delete()
    return RankRead(rank_id=r.rank_id, name=r.name)
