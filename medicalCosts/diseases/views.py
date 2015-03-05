from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from diseases.models import Operation, Procedure, Disease

from rest_framework import viewsets
from diseases.serializers import DiseaseSerializer, ProcedureSerializer, OperationSerializer

def index(request):
  return render(request, 'diseases/index.html', { 'diseases': Disease.objects.order_by('name') })

def disease(request, disease_id):
  disease = get_object_or_404(Disease, pk=disease_id)
  return render(request, 'diseases/disease.html', {'disease': disease})

def add_disease(request):
  try:
    d = Disease.objects.get(name__iexact=request.POST['name'])
  except (KeyError):
    return render(request,
      'diseases/index.html',
      { 'diseases': Disease.objects.order_by('name'),
      'error_message': "Please enter a disease name." })
  except (Disease.DoesNotExist):
    d = Disease(name=request.POST['name'])
    d.save()
    return HttpResponseRedirect(reverse('diseases:disease', args=(d.id,)))
  else:
    return render(request,
      'diseases/index.html',
      { 'diseases': Disease.objects.order_by('name'),
      'error_message': "Please enter a unique disease name" })


def procedure(request, procedure_id):
  procedure = get_object_or_404(Procedure, pk=procedure_id)
  return render(request, 'diseases/procedure.html', {'procedure': procedure})

def operation(request, operation_id):
  operation = get_object_or_404(Operation, pk=operation_id)
  return render(request, 'diseases/operation.html', {'operation': operation})


class DiseaseViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows diseases to be viewed or edited.
  """
  queryset = Disease.objects.all()
  serializer_class = DiseaseSerializer


class ProcedureViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows procedures to be viewed or edited.
  """
  queryset = Procedure.objects.all()
  serializer_class = ProcedureSerializer

class OperationViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows operations to be viewed or edited.
  """
  queryset = Operation.objects.all()
  serializer_class = OperationSerializer
