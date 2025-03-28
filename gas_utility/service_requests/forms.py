from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ["request_type", "description", "attachment"]  
    def __init__(self, *args, **kwargs):
        super(ServiceRequestForm, self).__init__(*args, **kwargs)
        self.fields["request_type"].widget.attrs.update({"placeholder": "Enter request type"})
        self.fields["description"].widget.attrs.update({"placeholder": "Describe the issue"})
