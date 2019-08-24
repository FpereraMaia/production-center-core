from django.db import models
from enum import Enum


class EmployeeWorkHours(Enum):
    FOUR = "4h"
    SIX = "6h"
    EIGHT = "8h"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    work_hours = models.CharField(
        max_length=3, choices=[(work_hour.value, work_hour.value) for work_hour in EmployeeWorkHours]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = '"employee"'
        ordering = ["name"]

    def __str__(self):
        return self.name
