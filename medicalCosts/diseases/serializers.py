from diseases.models import Operation, Procedure, Disease
from rest_framework import serializers


class DiseaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disease
        fields = ('url', 'name')


class ProcedureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Procedure
        fields = ('url', 'name', 'disease')


class OperationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Operation
        fields = ('url', 'procedure', 'location', 'cost', 'date')
