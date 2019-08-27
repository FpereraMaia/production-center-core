from model_mommy import mommy
from django_elasticsearch_dsl.documents import DocType
from production_center_core.final_product.models import FinalProduct
from production_center_core.employee.models import Employee
from production_center_core.raw_material.models import RawMaterial


def test_should_get_final_products(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        final_product = mommy.make(FinalProduct, make_m2m=True)
        response = client.get("/api/v1/final-products/")
        assert response.status_code == 200
        assert final_product.name == response.json()["results"][0]["name"]


def test_should_get_empty_final_products(db, client):
    response = client.get("/api/v1/final-products/")
    assert response.status_code == 200
    assert response.json()["count"] == 0


def test_should_get_final_products_by_id(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(FinalProduct)
        response = client.get("/api/v1/final-products/1/")
        assert response.status_code == 200
        assert response.json()["id"] == 1


def test_shouldnt_get_final_products_by_id(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(FinalProduct)
        response = client.get("/api/v1/final-products/A/")
        assert response.status_code == 404
        assert response.json() == {"detail": "Não encontrado."}


def test_should_create_final_products(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(Employee)
        mommy.make(RawMaterial)
        response = client.post(
            "/api/v1/final-products/", data={"name": "Cadeira", "employee": 1, "raw_materials": [1]}
        )
        assert response.status_code == 201
        assert response.json()["name"] == "Cadeira"


def test_shouldnt_create_final_products(db, client):
    response = client.post("/api/v1/final-products/")
    assert response.status_code == 400
    assert response.json() == {
        "name": ["Este campo é obrigatório."],
        "employee": ["Este campo é obrigatório."],
        "raw_materials": ["Esta lista não pode estar vazia."],
    }


def test_shouldnt_create_final_products_with_wrong_raw_materials_and_wrong_employee(db, client):
    response = client.post("/api/v1/final-products/", data={"name": "Cadeira", "employee": 1, "raw_materials": [9]})
    assert response.status_code == 400
    assert response.json() == {
        "employee": ['Pk inválido "1" - objeto não existe.'],
        "raw_materials": ['Pk inválido "9" - objeto não existe.'],
    }


def test_edit_raw_materials_by_put_method(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(FinalProduct, make_m2m=True)
        mommy.make(RawMaterial)
        response = client.put(
            "/api/v1/final-products/1/",
            data={"name": "string", "employee": 1, "raw_materials": [4]},
            content_type="application/json",
        )
        assert response.status_code == 200
        assert len(response.json()["raw_materials_related"]) == 1
        assert response.json()["raw_materials_related"][0]["id"] == 4


def test_shouldnt_edit_final_products_by_put_method_didnt_send_employee(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(FinalProduct, make_m2m=True)
        response = client.put(
            "/api/v1/final-products/1/", data={"name": "string", "raw_materials": [4]}, content_type="application/json"
        )
        assert response.status_code == 400
        assert response.json() == {"employee": ["Este campo é obrigatório."]}


def test_shouldnt_edit_final_products_by_put_method_didnt_send_raw_materials(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(FinalProduct, make_m2m=True)
        response = client.put(
            "/api/v1/final-products/1/", data={"name": "string", "raw_materials": []}, content_type="application/json"
        )
        assert response.status_code == 400
        assert response.json() == {
            "employee": ["Este campo é obrigatório."],
            "raw_materials": ["Esta lista não pode estar vazia."],
        }


def test_edit_final_product_by_patch_method(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(FinalProduct, make_m2m=True)
        response = client.patch("/api/v1/final-products/1/", data={"name": "VISH"}, content_type="application/json")
        assert response.status_code == 200
        assert response.json()["name"] == "VISH"


def test_edit_final_product_by_patch_method_only_raw_materials(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        raw_material = mommy.make(RawMaterial)
        final_product = mommy.make(FinalProduct, make_m2m=True)
        assert final_product.raw_materials.all().count() > 1
        response = client.patch(
            "/api/v1/final-products/1/", data={"raw_materials": [raw_material.id]}, content_type="application/json"
        )
        assert response.status_code == 200
        assert len(response.json()["raw_materials"]) == 1


def test_delete_final_products(db, client, mocker):
    with mocker.patch.object(DocType, "bulk", return_value=True):
        mommy.make(FinalProduct)
        response = client.delete("/api/v1/final-products/1/")
        assert response.status_code == 204
        assert FinalProduct.objects.all().count() == 0


def test_shouldnt_delete_final_products(db, client):
    response = client.delete("/api/v1/final-products/1/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Não encontrado."}
