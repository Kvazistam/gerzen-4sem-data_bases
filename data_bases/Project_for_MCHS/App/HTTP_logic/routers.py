from App.HTTP_logic.CRUD_Operation import router_operation
from App.HTTP_logic.CRUD_attestation import router_attestation
from App.HTTP_logic.CRUD_employee import router_employee
from App.HTTP_logic.CRUD_employee_exercise import router_employee_exercise
from App.HTTP_logic.CRUD_exercise import router_exercise
from App.HTTP_logic.CRUD_exercise_type import router_exercise_type
from App.HTTP_logic.CRUD_position import router_position
from App.HTTP_logic.CRUD_rank import router_rank
from App.HTTP_logic.CRUD_report import router_report

list_routers = [router_attestation, router_employee, router_employee_exercise, router_exercise, router_exercise_type, router_operation, router_position, router_rank, router_report]