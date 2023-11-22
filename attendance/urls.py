from django.urls import path
from .views import ClassGroupListView, ClassGroupDetailView, ClassSessionDetailView, ClassGroupCreateView, ClassGroupUpdateView

urlpatterns = [
    path("", ClassGroupListView.as_view(), name="classgroup_list"),
    path("<int:pk>/", ClassGroupDetailView.as_view(), name="class_sessions"),
    path("class_session/<int:pk>/", ClassSessionDetailView.as_view(), name="attendance_records"),
    path("create_classgroup/", ClassGroupCreateView.as_view(), name="create_classgroup"),
    path("update_classgroup/<int:pk>/", ClassGroupUpdateView.as_view(), name="update_classgroup"),
]
 