from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Student, Teacher, ClassGroup, ClassSession, Attendance
from .forms import ClassGroupCreationForm, ClassGroupUpdateForm


# Create your views here.
class ClassGroupCreateView(CreateView):
    model = ClassGroup
    form_class = ClassGroupCreationForm
    template_name = "attendance/classgroup_create.html"
    success_url = "/attendance"

class ClassGroupUpdateView(UpdateView):
    model = ClassGroup
    form_class = ClassGroupUpdateForm
    template_name = "attendance/classgroup_update.html"
    success_url = "/attendance"

class ClassGroupListView(ListView):
    model = ClassGroup
    template_name = "attendance/classgroup_list.html"

    
class ClassGroupDetailView(DetailView):
    model = ClassGroup
    template_name = "attendance/classgroup_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["class_sessions"] = ClassSession.objects.filter(class_group=self.object)
        return context


class ClassSessionDetailView(DetailView):
    model = ClassSession
    template_name = "attendance/classsession_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["attendance_records"] = Attendance.objects.filter(class_session=self.object)
        return context
