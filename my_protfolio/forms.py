from django import forms
from .models import Sk_cv
class skfile(forms.ModelForm):
    class Meta:
        model=Sk_cv
        fields = "__all__" 
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    message = forms.CharField(required=False,widget=forms.Textarea)