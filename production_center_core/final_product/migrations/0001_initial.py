# Generated by Django 2.2.4 on 2019-08-25 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [("employee", "0001_initial"), ("raw_material", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="FinalProduct",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "employee",
                    models.ForeignKey(
                        default="TESTE", on_delete=django.db.models.deletion.SET_DEFAULT, to="employee.Employee"
                    ),
                ),
                ("raw_materials", models.ManyToManyField(to="raw_material.RawMaterial")),
            ],
            options={"db_table": '"final_product"', "ordering": ["name"]},
        )
    ]
