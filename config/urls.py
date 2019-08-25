"""production_center_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# from rest_framework_swagger.views import get_swagger_view

from production_center_core.raw_material.views import RawMaterialViewSet
from production_center_core.employee.views import EmployeeViewSet
from production_center_core.final_product.views import FinalProductViewSet

app_name = "production_center_core"
api_version = "v1"
# schema_view = get_swagger_view(title="Production Center API")

router = routers.DefaultRouter()
router.register(r"raw-materials", RawMaterialViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"final-products", FinalProductViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Production Center API",
        default_version=api_version,
        description="An API to manage the entities Raw Material, Employee, Final Product and generate reports for.",
        terms_of_service="http://generator.lorem-ipsum.info/terms-and-conditions",
        contact=openapi.Contact(email="felipepqm@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


patterns = (
    [
        path("swagger", schema_view.with_ui("swagger", cache_timeout=0)),
        path("redoc", schema_view.with_ui("redoc", cache_timeout=0)),
        path("api/v1/", include(router.urls, None)),
    ],
    api_version,
)

urlpatterns = [path("", include(patterns))]
