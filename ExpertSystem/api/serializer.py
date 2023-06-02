from rest_framework import serializers
from .models import Result

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Result
        fields=('id','soft','hard','boot','problem','solution')



