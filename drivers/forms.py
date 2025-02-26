from django import forms
from datetime import datetime
from drivers.models import Bol, ServiceRequest, ServiceRequestImage, MileageReport, Truck, Trailer, Shipper, Customer, DemurrageReason, Product, ServiceRequestProblem
from django.forms.models import inlineformset_factory
from django.conf import settings
from datetime import datetime
import pytz


class BolForm(forms.ModelForm):
    truck = forms.ModelChoiceField(required=True, queryset=Truck.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_truck = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Truck Number'}))
    trailer_1 = forms.ModelChoiceField(required=False, queryset=Trailer.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_trailer_1 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Trailer'}))
    trailer_2 = forms.ModelChoiceField(required=False, queryset=Trailer.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_trailer_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Trailer'}))
    shipper = forms.ModelChoiceField(required=True, queryset=Shipper.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_shipper = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Shipper'}))
    customer = forms.ModelChoiceField(required=True, queryset=Customer.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_customer = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Customer'}))
    demurrage_reason = forms.ModelChoiceField(required=False, queryset=DemurrageReason.objects.all().order_by('reason'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_demurrage_reason = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Demurrage Reason'}))
    product = forms.ModelChoiceField(required=True, queryset=Product.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_product = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Customer'}))
    arrive_at = forms.CharField(required=False)
    depart_at = forms.CharField(required=False)

    class Meta:
        model = Bol
        exclude = ['created_by', 'completed_by', 'completed_at']

    def clean_arrive_at(self):
        if self.cleaned_data['arrive_at']:
            local = pytz.timezone (settings.TIME_ZONE)
            arrive_at = datetime.strptime(self.cleaned_data['arrive_at'], '%d %B %Y - %H:%M')
            return local.localize(arrive_at)

    def clean_depart_at(self):
        if self.cleaned_data['depart_at']:
            local = pytz.timezone (settings.TIME_ZONE)
            depart_at = datetime.strptime(self.cleaned_data['depart_at'], '%d %B %Y - %H:%M')
            return local.localize(depart_at)

    def clean(self):
        cleaned_data = super(BolForm, self).clean()

        if cleaned_data.get("arrive_at") and cleaned_data.get("depart_at") and cleaned_data.get("arrive_at") > cleaned_data.get("depart_at"):
            msg = u"Departure time must be after Arrival time"
            self.add_error('arrive_at', msg)
            self.add_error('depart_at', msg)

        # Remove custom field error to handle in view
        if 'truck' in self._errors:
            valid = True
            for error in self._errors['truck']:
                if 'Select a valid choice.' in error:
                    valid = False
                    break
            if not valid:
                del self._errors['truck']
        if 'trailer_1' in self._errors:
            del self._errors['trailer_1']
        if 'trailer_2' in self._errors:
            del self._errors['trailer_2']
        if 'shipper' in self._errors:
            valid = True
            for error in self._errors['shipper']:
                if 'Select a valid choice.' in error:
                    valid = False
                    break
            if not valid:
                del self._errors['shipper']
        if 'customer' in self._errors:
            valid = True
            for error in self._errors['customer']:
                if 'Select a valid choice.' in error:
                    valid = False
                    break
            if not valid:
                del self._errors['customer']
        if 'demurrage_reason' in self._errors:
            del self._errors['demurrage_reason']
        if 'product' in self._errors:
            valid = True
            for error in self._errors['product']:
                if 'Select a valid choice.' in error:
                    valid = False
                    break
            if not valid:
                del self._errors['product']

        return cleaned_data


class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        exclude = ['created_by', 'completed_by', 'completed_at', 'priority']


class ServiceRequestImageForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestImage
        fields = '__all__'

ServiceRequestImageFormSet = inlineformset_factory(ServiceRequest, ServiceRequestImage, form=ServiceRequestImageForm, extra=0)


class ProblemForm(forms.ModelForm):
    problem = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = ServiceRequestProblem
        fields = '__all__'

ProblemFormSet = inlineformset_factory(ServiceRequest, ServiceRequestProblem, form=ProblemForm, extra=6)
NoExtraProblemFormSet = inlineformset_factory(ServiceRequest, ServiceRequestProblem, form=ProblemForm, extra=0)


class MileageReportForm(forms.ModelForm):
    truck = forms.ModelChoiceField(required=True, queryset=Truck.objects.all().order_by('name'), widget=forms.Select(attrs={'class':'form-control other-select'}))
    new_truck = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control other-input hidden', 'placeholder':'New Truck Number'}))

    class Meta:
        model = MileageReport
        exclude = ['created_by']

    def clean(self):
        cleaned_data = super(MileageReportForm, self).clean()

        # Remove custom field error to handle in view
        if 'truck' in self._errors:
            valid = True
            for error in self._errors['truck']:
                if 'Select a valid choice.' in error:
                    valid = False
                    break
            if not valid:
                del self._errors['truck']
