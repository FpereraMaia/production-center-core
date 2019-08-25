from django.db import models
from production_center_core.employee.models import Employee
from production_center_core.raw_material.models import RawMaterial


class FinalProduct(models.Model):
    name = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)
    raw_materials = models.ManyToManyField(RawMaterial)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"final_product"'
        ordering = ["name"]

    def __str__(self):
        return self.name
