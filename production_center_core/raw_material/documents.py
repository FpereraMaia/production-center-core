from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import RawMaterial


@registry.register_document
class RawMaterialDocument(Document):
    class Index:
        name = "raw_materials"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = RawMaterial
        fields = ["name", "quantity_in_stock"]
