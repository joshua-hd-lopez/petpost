from django import forms

class Forms(forms.Form):
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    breed = forms.CharField(max_length=255)
    photo = forms.ImageField(required=False)


