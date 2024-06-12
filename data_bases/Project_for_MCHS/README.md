# Проект для МЧС
В этой директории реализованна возможность взаимодействия с базой данной посредством REST API на языке python. Для реализации работы с базой данных была использована библиотека Pony ORM, выбор ее обусловлен ее достаточно легковесностью, тк запросы реализованны самые простые, SQLAlchemy на мой взгляд здесь была бы лишней. Для реализации REST API была выбрана библиотека FAST API, так же в силу своей легковесности. 

В итоге были реализованы запросы к каждой таблице предметной области которые реализуют следующий функционал: 
* Добавление сущности
* Выбор всех сущностей
* Выбор одной сущности по id
* Обновление сущности
* Удаление сущности 

Таким образом представленный API реализует архитектуру CRUD, что и требовалось в задании. 

Данные передаются с помощью JSON форм, для просмотра требуемых аргументов в запросе можно найти описание форм в папке Mymodels.

Ниже представлены возможные ```curl``` запросы  к Нашему API.


Конечно, вот запросы `curl` для CRUD операций по каждой сущности в вашем приложении:

### Position

**Create Position:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/positions/' -H 'Content-Type: application/json' -d '{"name": "Manager", "group": "Admin"}'
```

**Read All Positions:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/positions/' -H 'Content-Type: application/json'
```

**Read Single Position:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/positions/{position_id}' -H 'Content-Type: application/json'
```

**Update Position:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/positions/{position_id}' -H 'Content-Type: application/json' -d '{"name": "Updated Manager", "group": "Updated Admin"}'
```

**Delete Position:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/positions/{position_id}' -H 'Content-Type: application/json'
```

### Rank

**Create Rank:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/ranks/' -H 'Content-Type: application/json' -d '{"name": "Lieutenant"}'
```

**Read All Ranks:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/ranks/' -H 'Content-Type: application/json'
```

**Read Single Rank:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/ranks/{rank_id}' -H 'Content-Type: application/json'
```

**Update Rank:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/ranks/{rank_id}' -H 'Content-Type: application/json' -d '{"name": "Updated Lieutenant"}'
```

**Delete Rank:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/ranks/{rank_id}' -H 'Content-Type: application/json'
```

### Employee

**Create Employee:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/employees/' -H 'Content-Type: application/json' -d '{"last_name": "Doe", "first_name": "John", "patronymic": "Smith", "date_of_birth": "1990-01-01", "position_id": 1, "rank_id": 1}'
```

**Read All Employees:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/employees/' -H 'Content-Type: application/json'
```

**Read Single Employee:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/employees/{employee_id}' -H 'Content-Type: application/json'
```

**Update Employee:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/employees/{employee_id}' -H 'Content-Type: application/json' -d '{"last_name": "Updated Doe", "first_name": "Updated John", "patronymic": "Updated Smith", "date_of_birth": "1990-01-01", "position_id": 1, "rank_id": 1}'
```

**Delete Employee:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/employees/{employee_id}' -H 'Content-Type: application/json'
```

### Attestation

**Create Attestation:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/attestations/' -H 'Content-Type: application/json' -d '{"employee_id": 1, "RPE_permission": true, "RPE_permission_deny_reason": null, "test_date": "2023-01-01", "permission_order_date": "2023-01-02", "permission_order_number": 123, "date": "2023-01-03"}'
```

**Read All Attestations:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/attestations/' -H 'Content-Type: application/json'
```

**Read Single Attestation:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/attestations/{attestation_id}' -H 'Content-Type: application/json'
```

**Update Attestation:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/attestations/{attestation_id}' -H 'Content-Type: application/json' -d '{"employee_id": 1, "RPE_permission": false, "RPE_permission_deny_reason": "Reason", "test_date": "2023-01-01", "permission_order_date": "2023-01-02", "permission_order_number": 123, "date": "2023-01-03"}'
```

**Delete Attestation:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/attestations/{attestation_id}' -H 'Content-Type: application/json'
```

### Exercise Type

**Create Exercise Type:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/exercise_types/' -H 'Content-Type: application/json' -d '{"name": "Fire Drill"}'
```

**Read All Exercise Types:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/exercise_types/' -H 'Content-Type: application/json'
```

**Read Single Exercise Type:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/exercise_types/{Exercise_type_id}' -H 'Content-Type: application/json'
```

**Update Exercise Type:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/exercise_types/{Exercise_type_id}' -H 'Content-Type: application/json' -d '{"name": "Updated Fire Drill"}'
```

**Delete Exercise Type:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/exercise_types/{Exercise_type_id}' -H 'Content-Type: application/json'
```

### Exercise

**Create Exercise:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/exercises/' -H 'Content-Type: application/json' -d '{"Exercise_type_id": 1, "date": "2023-01-01", "address": "123 Main St", "RFE_type": "Type A"}'
```

**Read All Exercises:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/exercises/' -H 'Content-Type: application/json'
```

**Read Single Exercise:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/exercises/{Exercise_id}' -H 'Content-Type: application/json'
```

**Update Exercise:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/exercises/{Exercise_id}' -H 'Content-Type: application/json' -d '{"Exercise_type_id": 1, "date": "2023-01-02", "address": "456 Main St", "RFE_type": "Type B"}'
```

**Delete Exercise:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/exercises/{Exercise_id}' -H 'Content-Type: application/json'
```

### Employee Exercise

**Create Employee Exercise:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/employee_exercises/' -H 'Content-Type: application/json' -d '{"exercise_id": 1, "employee_id": 1}'
```

**Read All Employee Exercises:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/employee_exercises/' -H 'Content-Type: application/json'
```

**Read Single Employee Exercise:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/employee_exercises/{id}' -H 'Content-Type: application/json'
```

**Update Employee Exercise:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/employee_exercises/{id}' -H 'Content-Type: application/json' -d '{"exercise_id": 2, "employee_id": 1}'
```

**Delete Employee Exercise:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/employee_exercises/{id}' -H 'Content-Type: application/json'
```

### Report

**Create Report:**
```sh
curl

 -X 'POST' 'http://127.0.0.1:8000/reports/' -H 'Content-Type: application/json' -d '{"attestation_id": 1, "exercise_id": 1, "description": "Initial report"}'
```

**Read All Reports:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/reports/' -H 'Content-Type: application/json'
```

**Read Single Report:**
```sh
curl -X 'GET' 'http://127.0.0.1:8000/reports/{report_id}' -H 'Content-Type: application/json'
```

**Update Report:**
```sh
curl -X 'PUT' 'http://127.0.0.1:8000/reports/{report_id}' -H 'Content-Type: application/json' -d '{"attestation_id": 1, "exercise_id": 1, "description": "Updated report"}'
```

**Delete Report:**
```sh
curl -X 'DELETE' 'http://127.0.0.1:8000/reports/{report_id}' -H 'Content-Type: application/json'
```