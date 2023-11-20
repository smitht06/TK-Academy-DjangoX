from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Student, Teacher, ClassGroup, ClassSession, Attendance

# Create your views here.
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

    

