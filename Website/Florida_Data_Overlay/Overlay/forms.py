from django import forms
from Overlay.models import Births

class UploadForm(forms.Form):
    upfile = forms.FileField(
        label='Select a file'
    )

class ChoosyForm(forms.Form):
    #right now is just counties
    #do a more complex queryset
    #with counties and years and attributes
    field = forms.ModelChoiceField(queryset = Births.objects.values('county').distinct())
