from rest_framework import serializers

from production_center_core.employee.serializers import EmployeeSerializer
from production_center_core.raw_material.serializers import RawMaterialSerializer

from .models import FinalProduct


class FinalProductSerializer(serializers.ModelSerializer):
    raw_materials = RawMaterialSerializer(many=True, read_only=True)
    employee = EmployeeSerializer(read_only=True)

    class Meta:
        model = FinalProduct
        fields = [field.name for field in FinalProduct._meta.fields] + ["raw_materials"]
