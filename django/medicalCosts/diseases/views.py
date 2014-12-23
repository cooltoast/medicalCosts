from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from diseases.models import Operation, Procedure, Disease

def operations(request):
  return render(request, 'diseases/operations.html', { 'operations': Operation.objects.order_by('-date') })

'''
def vendor(request, vendor_id):
  vendor = get_object_or_404(Vendor, pk=vendor_id)
  return render(request, 'diseases/vendor.html', {'vendor': vendor})
'''
