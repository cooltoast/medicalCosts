from django.contrib import admin
from diseases.models import Operation, Procedure, Disease

# Register your models here.
class OperationInline(admin.TabularInline):
  model = Operation
  extra = 3

class ProcedureAdmin(admin.ModelAdmin):
  inlines = [OperationInline]
  list_display = ('name', 'disease')

class ProcedureInline(admin.TabularInline):
  model = Procedure
  extra = 3

class DiseaseAdmin(admin.ModelAdmin):
  inlines = [ProcedureInline]

admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Procedure, ProcedureAdmin)
