from django import forms

from django.forms import SelectDateWidget
# from django.forms.extras.widgets Django < 1.9

class Inputlog(forms.Form):
    light= forms.CharField()
    


