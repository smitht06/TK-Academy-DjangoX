from django import forms
from .models import ClassGroup

class ClassGroupCreationForm(forms.ModelForm):
    class Meta:
        model = ClassGroup
        fields = ("teacher", "students", "level", "day_of_week")





