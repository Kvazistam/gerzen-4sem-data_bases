from fastapi import HTTPException, APIRouter
from pony.orm import db_session, select
from typing import List


from Classes.MyModels import ReportRead, ReportCreate
from Classes.ORM_classes import Exercise, Report

router_report = APIRouter()
# CRUD operations for Report

@router_report.post("/reports/", response_model=ReportRead)
@db_session
def create_report(report: ReportCreate):
    exercise = Exercise.get(Exercise_id=report.exercise_id)
    if not exercise:
        raise HTTPException(status_code=400, detail="Invalid Exercise ID")
    new_report = Report(
        exercise=exercise,
        start_date=report.start_date,
        finish_date=report.finish_date,
        count_plan=report.count_plan,
        count_actual=report.count_actual,
        count_reason=report.count_reason,
        comment=report.comment
    )
    return ReportRead(
        Report_id=new_report.Report_id,
        exercise_id=new_report.exercise.Exercise_id,
        start_date=new_report.start_date,
        finish_date=new_report.finish_date,
        count_plan=new_report.count_plan,
        count_actual=new_report.count_actual,
        count_reason=new_report.count_reason,
        comment=new_report.comment
    )

@router_report.get("/reports/", response_model=List[ReportRead])
@db_session
def read_reports():
    reports = select(r for r in Report)[:]
    return [ReportRead(
        Report_id=r.Report_id,
        exercise_id=r.exercise.Exercise_id,
        start_date=r.start_date,
        finish_date=r.finish_date,
        count_plan=r.count_plan,
        count_actual=r.count_actual,
        count_reason=r.count_reason,
        comment=r.comment
    ) for r in reports]

@router_report.get("/reports/{report_id}", response_model=ReportRead)
@db_session
def read_report(report_id: int):
    report = Report.get(Report_id=report_id)
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")
    return ReportRead(
        Report_id=report.Report_id,
        exercise_id=report.exercise.Exercise_id,
        start_date=report.start_date,
        finish_date=report.finish_date,
        count_plan=report.count_plan,
        count_actual=report.count_actual,
        count_reason=report.count_reason,
        comment=report.comment
    )

@router_report.put("/reports/{report_id}", response_model=ReportRead)
@db_session
def update_report(report_id: int, report: ReportCreate):
    r = Report.get(Report_id=report_id)
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    exercise = Exercise.get(Exercise_id=report.exercise_id)
    if not exercise:
        raise HTTPException(status_code=400, detail="Invalid Exercise ID")
    r.exercise = exercise
    r.start_date = report.start_date
    r.finish_date = report.finish_date
    r.count_plan = report.count_plan
    r.count_actual = report.count_actual
    r.count_reason = report.count_reason
    r.comment = report.comment
    return ReportRead(
        Report_id=r.Report_id,
        exercise_id=r.exercise.Exercise_id,
        start_date=r.start_date,
        finish_date=r.finish_date,
        count_plan=r.count_plan,
        count_actual=r.count_actual,
        count_reason=r.count_reason,
        comment=r.comment
    )

@router_report.delete("/reports/{report_id}", response_model=ReportRead)
@db_session
def delete_report(report_id: int):
    r = Report.get(Report_id=report_id)
    if not r:
        raise HTTPException(status_code=404, detail="Report not found")
    r.delete()
    return ReportRead(
        Report_id=r.Report_id,
        exercise_id=r.exercise.Exercise_id,
        start_date=r.start_date,
        finish_date=r.finish_date,
        count_plan=r.count_plan,
        count_actual=r.count_actual,
        count_reason=r.count_reason,
        comment=r.comment
    )