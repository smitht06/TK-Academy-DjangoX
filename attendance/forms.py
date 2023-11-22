from django import forms
from .models import ClassGroup, Teacher, Student, Level, DayOfWeek


class ClassGroupCreationForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    days_of_week = forms.ModelMultipleChoiceField(
        queryset=DayOfWeek.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = ClassGroup
        fields = [
            "name",
            "teacher",
            "students",
            "level",
            "days_of_week",
        ]  # Include other fields as needed


class ClassGroupUpdateForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    days_of_week = forms.ModelMultipleChoiceField(
        queryset=DayOfWeek.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )

    class Meta:
        model = ClassGroup
        fields = [
            "name",
            "teacher",
            "students",
            "level",
            "day_of_week",
        ]  # Include other fields as needed





