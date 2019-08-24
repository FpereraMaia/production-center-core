from django.db import models


class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    quantity_in_stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"raw_material"'
        ordering = ["name"]

    def __str__(self):
        return self.name
