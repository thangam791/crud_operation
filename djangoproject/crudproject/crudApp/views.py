from rest_framework import response,decorators
from crudApp.models import employee
from crudApp.serializers import EmpSerializer

# Create your views here.
@decorators.api_view(['GET'])
def emp_view(request):
    emp_query = employee.objects.all()
    emp_serializer = EmpSerializer(emp_query,many=True)
    return response.Response(emp_serializer.data)

@decorators.api_view(['POST'])
def emp_create(request):
    emp_dict = {
        'name':request.data['name'],
        'email':request.data['email']
         }
    emp_serializer = EmpSerializer(data = emp_dict)
    if emp_serializer.is_valid():
        emp_serializer.save()
        return response.Response('Employee Created successfully!')
    return response.Response('Please give valid details.')

@decorators.api_view(['PUT'])
def emp_update(request,id=0):
    emp_query = employee.objects.get(id=id)
    emp_dict = {
        'name':request.data['name'],
        'email':request.data['email']
         }
    emp_serializer = EmpSerializer(emp_query,data = emp_dict)
    if emp_serializer.is_valid():
        emp_serializer.save()
        return response.Response('Employee updated successfully!')
    return response.Response('Please give valid details.')

@decorators.api_view(['DELETE'])
def emp_delete(request,id=0):
    emp_query = employee.objects.filter(id=id)
    if emp_query.count() > 0:
        emp_query.delete()
        return response.Response('Deleted Successfully!')
    return response.Response('Please give valid details.')

