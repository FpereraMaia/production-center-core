from rest_framework.viewsets import ModelViewSet

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(ModelViewSet):
    """
       retrieve:
           Return the given employee.

       list:
           Return a list of all employees.

       create:
           Create a new employee.

       destroy:
           Delete an employee.

       update:
           Update an employee.

       partial_update:
           Update an employee.
       """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
