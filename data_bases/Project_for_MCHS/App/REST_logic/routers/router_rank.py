from typing import List

from fastapi import APIRouter

from App.REST_logic.CRUD.CRUD_rank import create_rank, read_ranks, read_rank, update_rank, delete_rank
from Classes.MyModels import RankCreate, RankRead

router_rank = APIRouter()


# CRUD operations for Rank
@router_rank.post("/ranks/", response_model=RankRead)
def create_rank_request(rank: RankCreate):
    return create_rank(rank)


@router_rank.get("/ranks/", response_model=List[RankRead])
def read_ranks_request():
    return read_ranks()


@router_rank.get("/ranks/{rank_id}", response_model=RankRead)
def read_rank_request(rank_id: int):
    return read_rank(rank_id)


@router_rank.put("/ranks/{rank_id}", response_model=RankRead)
def update_rank_request(rank_id: int, rank: RankCreate):
    return update_rank(rank_id, rank)


@router_rank.delete("/ranks/{rank_id}", response_model=RankRead)
def delete_rank_request(rank_id: int):
    return delete_rank(rank_id)
