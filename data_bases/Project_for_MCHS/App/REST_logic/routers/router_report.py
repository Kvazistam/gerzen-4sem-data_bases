from typing import List

from fastapi import APIRouter

from App.REST_logic.CRUD.CRUD_report import create_report, read_reports, read_report, update_report, delete_report
from Classes.MyModels import ReportRead, ReportCreate

router_report = APIRouter()


# CRUD operations for Report

@router_report.post("/reports/", response_model=ReportRead)
def create_report_request(report: ReportCreate):
    return create_report(report)


@router_report.get("/reports/", response_model=List[ReportRead])
def read_reports_request():
    return read_reports()


@router_report.get("/reports/{report_id}", response_model=ReportRead)
def read_report_request(report_id: int):
    return read_report(report_id)


@router_report.put("/reports/{report_id}", response_model=ReportRead)
def update_report_request(report_id: int, report: ReportCreate):
    return update_report(report_id, report)


@router_report.delete("/reports/{report_id}", response_model=ReportRead)
def delete_report_request(report_id: int):
    return delete_report(report_id)
