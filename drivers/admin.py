from django.contrib import admin
from django.contrib.auth.models import User, Group
from drivers.models import *
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm

admin.site.site_header = "Double D Distribution Admin"
admin.site.site_title = "Admin"

admin.site.unregister(Group)

class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['is_staff'].help_text = 'Designates whether this user can log onto company website'

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class UserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.form = CustomUserChangeForm
        self.inlines = [UserProfileInline]
        return super(UserAdmin, self).change_view(*args, **kwargs)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class ServiceRequestProblemInline(admin.TabularInline):
    model = ServiceRequestProblem

class ServiceRequestImageInline(admin.TabularInline):
    model = ServiceRequestImage

class ServiceRequestAdmin(admin.ModelAdmin):
    inlines = [
        ServiceRequestProblemInline,
        ServiceRequestImageInline,
    ]

admin.site.register(Bol)
admin.site.register(Truck)
admin.site.register(Trailer)
admin.site.register(Shipper)
admin.site.register(Customer)
admin.site.register(DemurrageReason)
admin.site.register(Product)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(MileageReport)
admin.site.register(AsphaltTrailerMeasurement)
admin.site.register(AsphaltTrailerOutage)
admin.site.register(CrudeTrailerLevel)
