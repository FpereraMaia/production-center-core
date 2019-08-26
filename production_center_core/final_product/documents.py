from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import FinalProduct
from production_center_core.raw_material.models import RawMaterial
from production_center_core.employee.models import Employee


@registry.register_document
class FinalProductDocument(Document):
    employee = fields.ObjectField(properties={"name": fields.TextField(), "work_hours": fields.TextField()})
    raw_materials = fields.NestedField(
        properties={"name": fields.TextField(), "quantity_in_stock": fields.IntegerField()}
    )

    class Index:
        name = "final_products"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = FinalProduct
        fields = ["name"]
        related_models = [Employee, RawMaterial]
