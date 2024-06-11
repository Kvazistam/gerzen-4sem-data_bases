# CRUD operations for Attestation
from typing import List

from fastapi import HTTPException, APIRouter
from pony.orm import db_session, select

from Classes.MyModels import AttestationRead, AttestationCreate
from Classes.ORM_classes import Employee, Attestation


router_attestation = APIRouter()

@router_attestation.post("/attestations/", response_model=AttestationRead)
@db_session
def create_attestation(attestation: AttestationCreate):
    employee = Employee.get(employee_id=attestation.employee_id)
    if not employee:
        raise HTTPException(status_code=400, detail="Invalid employee ID")
    new_attestation = Attestation(
        employee=employee,
        RPE_permission=attestation.RPE_permission,
        RPE_permission_deny_reason=attestation.RPE_permission_deny_reason,
        test_date=attestation.test_date,
        permission_order_date=attestation.permission_order_date,
        permission_order_number=attestation.permission_order_number,
        date=attestation.date
    )
    return AttestationRead(
        attestation_id=new_attestation.attestation_id,
        employee_id=new_attestation.employee.employee_id,
        RPE_permission=new_attestation.RPE_permission,
        RPE_permission_deny_reason=new_attestation.RPE_permission_deny_reason,
        test_date=new_attestation.test_date,
        permission_order_date=new_attestation.permission_order_date,
        permission_order_number=new_attestation.permission_order_number,
        date=new_attestation.date
    )


@router_attestation.get("/attestations/", response_model=List[AttestationRead])
@db_session
def read_attestations():
    attestations = select(a for a in Attestation)[:]
    return [AttestationRead(
        attestation_id=a.attestation_id,
        employee_id=a.employee.employee_id,
        RPE_permission=a.RPE_permission,
        RPE_permission_deny_reason=a.RPE_permission_deny_reason,
        test_date=a.test_date,
        permission_order_date=a.permission_order_date,
        permission_order_number=a.permission_order_number,
        date=a.date
    ) for a in attestations]


@router_attestation.get("/attestations/{attestation_id}", response_model=AttestationRead)
@db_session
def read_attestation(attestation_id: int):
    attestation = Attestation.get(attestation_id=attestation_id)
    if not attestation:
        raise HTTPException(status_code=404, detail="Attestation not found")
    return AttestationRead(
        attestation_id=attestation.attestation_id,
        employee_id=attestation.employee.employee_id,
        RPE_permission=attestation.RPE_permission,
        RPE_permission_deny_reason=attestation.RPE_permission_deny_reason,
        test_date=attestation.test_date,
        permission_order_date=attestation.permission_order_date,
        permission_order_number=attestation.permission_order_number,
        date=attestation.date
    )


@router_attestation.put("/attestations/{attestation_id}", response_model=AttestationRead)
@db_session
def update_attestation(attestation_id: int, attestation: AttestationCreate):
    a = Attestation.get(attestation_id=attestation_id)
    if not a:
        raise HTTPException(status_code=404, detail="Attestation not found")
    employee = Employee.get(employee_id=attestation.employee_id)
    if not employee:
        raise HTTPException(status_code=400, detail="Invalid employee ID")
    a.employee = employee
    a.RPE_permission = attestation.RPE_permission
    a.RPE_permission_deny_reason = attestation.RPE_permission_deny_reason
    a.test_date = attestation.test_date
    a.permission_order_date = attestation.permission_order_date
    a.permission_order_number = attestation.permission_order_number
    a.date = attestation.date
    return AttestationRead(
        attestation_id=a.attestation_id,
        employee_id=a.employee.employee_id,
        RPE_permission=a.RPE_permission,
        RPE_permission_deny_reason=a.RPE_permission_deny_reason,
        test_date=a.test_date,
        permission_order_date=a.permission_order_date,
        permission_order_number=a.permission_order_number,
        date=a.date
    )


@router_attestation.delete("/attestations/{attestation_id}", response_model=AttestationRead)
@db_session
def delete_attestation(attestation_id: int):
    a = Attestation.get(attestation_id=attestation_id)
    if not a:
        raise HTTPException(status_code=404, detail="Attestation not found")
    a.delete()
    return AttestationRead(
        attestation_id=a.attestation_id,
        employee_id=a.employee.employee_id,
        RPE_permission=a.RPE_permission,
        RPE_permission_deny_reason=a.RPE_permission_deny_reason,
        test_date=a.test_date,
        permission_order_date=a.permission_order_date,
        permission_order_number=a.permission_order_number,
        date=a.date
    )
