from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from diseases.models import Operation, Procedure, Disease

def index(request):
  return render(request, 'diseases/index.html', { 'diseases': Disease.objects.order_by('name') })

def disease(request, disease_id):
  disease = get_object_or_404(Disease, pk=disease_id)
  return render(request, 'diseases/disease.html', {'disease': disease})

def procedure(request, procedure_id):
  procedure = get_object_or_404(Procedure, pk=procedure_id)
  return render(request, 'diseases/procedure.html', {'procedure': procedure})

def operation(request, operation_id):
  operation = get_object_or_404(Operation, pk=operation_id)
  return render(request, 'diseases/operation.html', {'operation': operation})
