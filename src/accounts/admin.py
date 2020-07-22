from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.options import ModelAdmin

#from ajax_select.admin import AjaxSelectAdmin
#from ajax_select import make_ajax_form

from patient_form.models import *
from .forms import *


# Register your models here.
class PatientDataAdmin(admin.StackedInline):
    model = Admission
    max_num = 1
    extra = 1

class UserProfileAdmin(admin.ModelAdmin):
#    class FullNameModelChoiceField(forms.ModelChoiceField):
#        def label_from_instance(self, obj):
#            return "%s" % (obj.full_name)

#    class ICNumberModelChoiceField(forms.ModelChoiceField):
#        def label_from_instance(self, obj):
#            return "%s" % (obj.ic_number)

#    def formfield_for_foreignkey(self, db_field, request, **kwargs):
#        if db_field.name == 'full_name':
#            return self.FullNameModelChoiceField(queryset=UserProfile.objects)
#        elif db_field.name == 'ic_number':
#            return self.ICNumberModelChoiceField(queryset=UserProfile.objects)

#        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = [
        'id',
        'username',
        'email',
        'full_name',
        'ic_number',
        'jkl',
        'eth',
#        'roles',
        'is_active',
        'is_staff'
    ]
#    list_filter = ['user']
    ModelAdmin.ordering = ('id',)
    search_fields = ['full_name']
#    form = UserProfileForm
#    form = make_ajax_form(UserProfile, {
#        'full_name': 'full_name'
#    })
    inlines = [
        PatientDataAdmin,
    ]

#    class Meta:
#        model = UserProfile


admin.site.register(Role)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(PatientProfile)
admin.site.register(FamilyProfile)
admin.site.register(StaffProfile)
