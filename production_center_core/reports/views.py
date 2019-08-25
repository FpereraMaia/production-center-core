from rest_framework import viewsets
from production_center_core.raw_material.services import RawMaterialService
from rest_framework.filters import BaseFilterBackend
import coreapi
from rest_framework.response import Response


class RawMaterialsSchema(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(name="quantity-in-stock", location="query", required=False, type="integer")]


class FinalProductsFilterSchema(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [
            coreapi.Field(name="employee_name", location="query", required=False, type="string"),
            coreapi.Field(name="raw_materials", location="query", required=False, type="string"),
        ]


class ReportsRawMaterialViewSet(viewsets.ViewSet):
    filter_backends = (RawMaterialsSchema,)

    def list(self, request, *args, **kwargs):
        quantity_in_stock_filter = request.query_params.get("quantity-in-stock", None)
        if quantity_in_stock_filter:
            return Response(RawMaterialService.get_less_than_quantity_stock(quantity_in_stock_filter))
        return Response(RawMaterialService.get_all(), status=200)


class ReportsFinalProduct(viewsets.ViewSet):
    filter_backends = (FinalProductsFilterSchema,)

    def list(self, request, *args, **kwargs):
        pass
