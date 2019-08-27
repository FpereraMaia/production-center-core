from model_mommy import mommy
from production_center_core.employee.models import Employee


def test_should_get_employee(db, client):
    employee = mommy.make(Employee)
    response = client.get("/api/v1/employees/")
    assert response.status_code == 200
    assert employee.name == response.json()["results"][0]["name"]


def test_should_get_empty_employee(db, client):
    response = client.get("/api/v1/employees/")
    assert response.status_code == 200
    assert response.json()["count"] == 0


def test_should_get_employee_by_id(db, client):
    mommy.make(Employee)
    response = client.get("/api/v1/employees/1/")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_shouldnt_get_employee_by_id(db, client):
    mommy.make(Employee)
    response = client.get("/api/v1/employees/A/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Não encontrado."}


def test_should_create_employee(db, client):
    response = client.post("/api/v1/employees/", data={"name": "batman", "work_hours": 4})
    assert response.status_code == 201
    assert response.json()["name"] == "batman"


def test_shouldnt_create_employee(db, client):
    response = client.post("/api/v1/employees/")
    assert response.status_code == 400
    assert response.json() == {"name": ["Este campo é obrigatório."], "work_hours": ["Este campo é obrigatório."]}


def test_create_employee_with_invalid_work_hour(db, client):
    response = client.post("/api/v1/employees/", data={"name": "batman", "work_hours": 10})
    assert response.status_code == 400
    assert response.json() == {"work_hours": ['"10" não é um escolha válido.']}


def test_edit_employee_by_put_method(db, client):
    mommy.make(Employee)
    response = client.put(
        "/api/v1/employees/1/", data={"name": "batman", "work_hours": 4}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json()["name"] == "batman"


def test_edit_employee_wrong_content_type(db, client):
    mommy.make(Employee)
    response = client.put("/api/v1/employees/1/", data={"name": "batman", "work_hours": 4})
    assert response.status_code == 415


def test_edit_employee_by_patch_method(db, client):
    mommy.make(Employee)
    response = client.patch("/api/v1/employees/1/", data={"name": "batman"}, content_type="application/json")
    assert response.status_code == 200
    assert response.json()["name"] == "batman"


def test_edit_employee_by_patch_method_change_work_hours(db, client):
    mommy.make(Employee)
    response = client.patch("/api/v1/employees/1/", data={"work_hours": 6}, content_type="application/json")
    assert response.status_code == 200
    assert response.json()["work_hours"] == 6


def test_delete_employee(db, client):
    mommy.make(Employee)
    response = client.delete("/api/v1/employees/1/")
    assert response.status_code == 204
    assert Employee.objects.all().count() == 0


def test_shouldnt_delete_employee(db, client):
    response = client.delete("/api/v1/employees/1/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Não encontrado."}
