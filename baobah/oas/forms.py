from django import forms
from .models import Oas
#DataFlair
class OasCreate(forms.ModelForm):
    class Meta:
        model = Oas
        fields = '__all__'