# -*- coding: utf-8 -*-
from django import forms

class UploadForm(forms.Form):
    upfile = forms.FileField(
        label='Select a file'
    )
