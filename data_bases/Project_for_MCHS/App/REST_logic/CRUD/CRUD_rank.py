from fastapi import HTTPException
from pony.orm import db_session, select, commit

from Classes.MyModels import RankCreate, RankRead
from Classes.ORM_classes import Rank


# CRUD operations for Rank
@db_session
def create_rank(rank: RankCreate):
    new_rank = Rank(name=rank.name)
    commit()
    return RankRead(rank_id=new_rank.rank_id, name=new_rank.name)


@db_session
def read_ranks():
    ranks = select(r for r in Rank)[:]
    return [RankRead(rank_id=r.rank_id, name=r.name) for r in ranks]


@db_session
def read_rank(rank_id: int):
    rank = Rank.get(rank_id=rank_id)
    if not rank:
        raise HTTPException(status_code=404, detail="Rank not found")
    return RankRead(rank_id=rank.rank_id, name=rank.name)


@db_session
def update_rank(rank_id: int, rank: RankCreate):
    r = Rank.get(rank_id=rank_id)
    if not r:
        raise HTTPException(status_code=404, detail="Rank not found")
    r.name = rank.name
    commit()
    return RankRead(rank_id=r.rank_id, name=r.name)


@db_session
def delete_rank(rank_id: int):
    r = Rank.get(rank_id=rank_id)
    if not r:
        raise HTTPException(status_code=404, detail="Rank not found")
    r.delete()
    return RankRead(rank_id=r.rank_id, name=r.name)
