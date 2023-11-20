from django.urls import path
from .views import ClassGroupListView, ClassGroupDetailView

urlpatterns = [
    path("", ClassGroupListView.as_view(), name="classgroup_list"),
    path("<int:pk>/", ClassGroupDetailView.as_view(), name="class_sessions"),
]
