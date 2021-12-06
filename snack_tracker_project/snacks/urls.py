from django.urls import path
from .views import SnackListView, SnackDateView

urlpatterns = [
    path("", SnackListView.as_view(), name = 'snack_list'),
    path("<int:pk>", SnackDateView.as_view(), name = 'snack_detail'),
]