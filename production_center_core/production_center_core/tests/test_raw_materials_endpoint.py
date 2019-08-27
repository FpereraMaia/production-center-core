from model_mommy import mommy
from production_center_core.raw_material.models import RawMaterial


def test_should_get_raw_material(db, client):
    raw_material = mommy.make(RawMaterial)
    response = client.get("/api/v1/raw-materials/")
    assert response.status_code == 200
    assert raw_material.name == response.json()["results"][0]["name"]


def test_should_get_empty_raw_materials(db, client):
    response = client.get("/api/v1/raw-materials/")
    assert response.status_code == 200
    assert response.json()["count"] == 0


def test_should_get_employee_by_id(db, client):
    mommy.make(RawMaterial)
    response = client.get("/api/v1/raw-materials/1/")
    assert response.status_code == 200
    assert response.json()["id"] == 1


def test_shouldnt_get_raw_materials_by_id(db, client):
    mommy.make(RawMaterial)
    response = client.get("/api/v1/employees/A/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Não encontrado."}


def test_should_create_raw_materials(db, client):
    response = client.post("/api/v1/raw-materials/", data={"name": "malte", "quantity_in_stock": 31})
    assert response.status_code == 201
    assert response.json()["name"] == "malte"


def test_shouldnt_create_raw_materials(db, client):
    response = client.post("/api/v1/raw-materials/")
    assert response.status_code == 400
    assert response.json() == {
        "name": ["Este campo é obrigatório."],
        "quantity_in_stock": ["Este campo é obrigatório."],
    }


def test_shouldnt_create_raw_materials_with_wrong_quantity_in_stock(db, client):
    response = client.post("/api/v1/raw-materials/", data={"name": "malte", "quantity_in_stock": -31})
    assert response.status_code == 400
    assert response.json() == {"quantity_in_stock": ["Certifque-se de que este valor seja maior ou igual a 1."]}


def test_edit_raw_materials_by_put_method(db, client):
    mommy.make(RawMaterial)
    response = client.put(
        "/api/v1/raw-materials/1/", data={"name": "malte", "quantity_in_stock": 4}, content_type="application/json"
    )
    assert response.status_code == 200
    assert response.json()["name"] == "malte"


def test_shouldnt_edit_raw_materials_by_put_method(db, client):
    mommy.make(RawMaterial)
    response = client.put("/api/v1/raw-materials/1/", data={"name": "malte"}, content_type="application/json")
    assert response.status_code == 400
    assert response.json() == {"quantity_in_stock": ["Este campo é obrigatório."]}


def test_edit_raw_materials_by_patch_method(db, client):
    mommy.make(RawMaterial)
    response = client.patch("/api/v1/raw-materials/1/", data={"name": "cerveja"}, content_type="application/json")
    assert response.status_code == 200
    assert response.json()["name"] == "cerveja"


def test_delete_raw_materials(db, client):
    mommy.make(RawMaterial)
    response = client.delete("/api/v1/raw-materials/1/")
    assert response.status_code == 204
    assert RawMaterial.objects.all().count() == 0


def test_shouldnt_delete_raw_materials(db, client):
    response = client.delete("/api/v1/raw-materials/1/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Não encontrado."}
