from django import forms
from Overlay.models import Births

class UploadForm(forms.Form):
    upfile = forms.FileField(
        label='Select a file'
    )
    
class BirthForm(forms.Form):
    years =             forms.MultipleChoiceField(widget = forms.CheckboxSelectMultiple,
                                                  choices = Births.objects.all()
                                                              .order_by('-year')
                                                              .values('year')
                                                              .distinct())
    '''
    counties =          forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple
                                                       Births.objects.all()
                                                      .values('county')
                                                      .distinct())
    
    ages =              forms.ModelMultipleChoiceField(Births.objects.all()
                                          .values('mothersAge')
                                          .distinct())
    
    edus =              forms.ModelMultipleChoiceField(Births.objects.all()
                                          .values('mothersEdu')
                                          .distinct())
    
    repeat_birth_bool = forms.ModelMultipleChoiceField(Births.objects.all()
                                          .values('isRepeat')
                                          .distinct())
    '''
