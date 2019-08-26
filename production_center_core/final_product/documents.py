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

    def get_queryset(self):
        return super().get_queryset().select_related(
            'employee', 'raw_materials'
        )

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the Car instance(s) from the related model.
        The related_models option should be used with caution because it can lead in the index
        to the updating of a lot of items.
        """
        if isinstance(related_instance, Employee):
            return related_instance.finalproduct_set.all()
        elif isinstance(related_instance, RawMaterial):
            return related_instance.finalproduct_set
