from rest_framework import serializers
from crudApp.models import employee

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields ='__all__'