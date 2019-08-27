from django.shortcuts import get_object_or_404

from production_center_core.final_product.models import FinalProduct


class FinalProductService:
    @staticmethod
    def create(data):
        final_product = FinalProduct()
        final_product.name = data["name"]
        final_product.employee = data["employee"]
        final_product.save()
        FinalProductService._add_all_raw_materials(final_product, data["raw_materials"])
        return final_product

    @staticmethod
    def update(final_product, data):
        final_product.employee = data["employee"]
        final_product.name = data["name"]
        FinalProductService._add_all_raw_materials(final_product, data["raw_materials"])
        return final_product

    @staticmethod
    def _add_all_raw_materials(final_product, raw_materials):
        final_product.raw_materials.clear()
        for raw_material in raw_materials:
            final_product.raw_materials.add(raw_material)

    @staticmethod
    def get_by_id(pk):
        return get_object_or_404(FinalProduct, pk=pk)

    # TODO CAN BE MUCH BETTER
    @staticmethod
    def partial_update(final_product, data):
        if data.get("name", None) is not None:
            final_product.name = data.get("name")
        elif data.get("raw_materials", None) is not None:
            FinalProductService._add_all_raw_materials(final_product, data.get("raw_materials"))
        elif data.get("employee", None) is not None:
            final_product.employee = data.get("employee")
        final_product.save()
        return final_product
