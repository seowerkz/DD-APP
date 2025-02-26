from django.contrib import admin
from shop.models import Part, WorkOrder, WorkPerformed

class PartInline(admin.TabularInline):
    model = WorkOrder.parts.through

class WorkPerformedInline(admin.TabularInline):
    model = WorkPerformed

class WorkOrderAdmin(admin.ModelAdmin):
    search_fields = ('unit_number',)
    exclude = ('work_performed',)
    inlines = [
        WorkPerformedInline,
        PartInline,
    ]

class PartAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Part, PartAdmin)
admin.site.register(WorkOrder, WorkOrderAdmin)
