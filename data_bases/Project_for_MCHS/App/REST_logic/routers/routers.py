from App.HTTP_logic.routers.router_attestation import router_attestation
from App.HTTP_logic.routers.router_employee import router_employee
from App.HTTP_logic.routers.router_employee_exercise import router_employee_exercise
from App.HTTP_logic.routers.router_exercise_type import router_exercise_type
from App.HTTP_logic.routers.router_exersize import router_exercise
from App.HTTP_logic.routers.router_position import router_position
from App.HTTP_logic.routers.router_rank import router_rank
from App.HTTP_logic.routers.router_report import router_report

list_routers = [router_attestation, router_employee, router_employee_exercise, router_exercise, router_exercise_type, router_position, router_rank, router_report]