from django import forms
from django.forms.models import inlineformset_factory
from django.conf import settings
from django.contrib.auth.models import User
from shop.models import WorkOrder, PartsUsed, Part, WorkOrderMechanics, WorkPerformed
from datetime import datetime
import pytz


class WorkOrderForm(forms.ModelForm):
    class Meta:
        model = WorkOrder
        exclude = ['created_by', 'completed_by', 'completed_at', 'updated_by', 'updated_at', 'finished_by', 'finished_at', 'parts']

class WorkPerformedForm(forms.ModelForm):
    work_performed = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = WorkPerformed
        fields = '__all__'

WorkPerformedFormSet = inlineformset_factory(WorkOrder, WorkPerformed, form=WorkPerformedForm, extra=1)

class MechanicForm(forms.ModelForm):
    mechanic = forms.ModelChoiceField(queryset=User.objects.filter(groups__name='shop').order_by("username"), required=False, widget=forms.Select(attrs={'class':'form-control'}))
    hours = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = WorkOrderMechanics
        fields = '__all__'

MechanicFormSet = inlineformset_factory(WorkOrder, WorkOrderMechanics, form=MechanicForm, extra=1)


class PartsUsedForm(forms.ModelForm):
    part = forms.ModelChoiceField(required=False, queryset=Part.objects.all().order_by("name"), widget=forms.Select(attrs={'class':'form-control part-select'}))
    quantity = forms.FloatField(required=False, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Quantity'}))
    new_part = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control new-part hidden', 'placeholder':'Part Name'}))

    def clean(self):
        super(PartsUsedForm, self).clean()
        # Remove part error to handle in view
        if 'part' in self._errors:
            del self._errors['part']
        return self.cleaned_data

    class Meta:
        model = PartsUsed
        fields = '__all__'

PartFormSet = inlineformset_factory(WorkOrder, PartsUsed, form=PartsUsedForm, extra=6)
