from rest_framework import serializers

from production_center_core.employee.serializers import EmployeeSerializer
from production_center_core.raw_material.serializers import RawMaterialSerializer
from production_center_core.final_product.services import FinalProductService

from .models import FinalProduct


class FinalProductSerializer(serializers.ModelSerializer):
    raw_materials_related = RawMaterialSerializer(many=True, source="raw_materials", required=False)
    employee_related = EmployeeSerializer(read_only=True, source="employee")

    class Meta:
        model = FinalProduct
        fields = [field.name for field in FinalProduct._meta.fields] + [
            "raw_materials",
            "employee_related",
            "raw_materials_related",
        ]

    def create(self, validated_data):
        return FinalProductService.create(validated_data)

    def update(self, instance, validated_data):
        return FinalProductService.update(instance, validated_data)
