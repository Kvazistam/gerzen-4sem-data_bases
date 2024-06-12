from typing import List

from fastapi import APIRouter

from App.REST_logic.CRUD.CRUD_attestation import create_attestation, read_attestations, read_attestation, \
    update_attestation, delete_attestation
from Classes.MyModels import AttestationRead, AttestationCreate

router_attestation = APIRouter()


# CRUD operations for Attestation
@router_attestation.post("/attestations/", response_model=AttestationRead)
def create_attestation_request(attestation: AttestationCreate):
    return create_attestation(attestation)


@router_attestation.get("/attestations/", response_model=List[AttestationRead])
def read_attestations_request():
    return read_attestations()


@router_attestation.get("/attestations/{attestation_id}", response_model=AttestationRead)
def read_attestation_request(attestation_id: int):
    return read_attestation(attestation_id)


@router_attestation.put("/attestations/{attestation_id}", response_model=AttestationRead)
def update_attestation_request(attestation_id: int, attestation: AttestationCreate):
    return update_attestation(attestation_id, attestation)


@router_attestation.delete("/attestations/{attestation_id}", response_model=AttestationRead)
def delete_attestation_request(attestation_id: int):
    return delete_attestation(attestation_id)
