from rest_framework import serializers

from production_center_core.employee.serializers import EmployeeSerializer
from production_center_core.raw_material.serializers import RawMaterialSerializer

from .models import FinalProduct


class FinalProductSerializer(serializers.ModelSerializer):
    # raw_materials = RawMaterialSerializer(many=True)
    raw_materials_related = RawMaterialSerializer(many=True, source="raw_materials", required=False)
    employee_related = EmployeeSerializer(read_only=True, source="employee")
    # employee = EmployeeSerializer(many=False, read_only=True, source='employee')

    class Meta:
        model = FinalProduct
        fields = [field.name for field in FinalProduct._meta.fields] + [
            "raw_materials",
            "employee_related",
            "raw_materials_related",
        ]

    def create(self, validated_data):
        final_product = FinalProduct()
        final_product.name = validated_data["name"]
        final_product.employee = validated_data["employee"]
        final_product.save()

        for raw_material in validated_data["raw_materials"]:
            final_product.raw_materials.add(raw_material)

        return final_product
