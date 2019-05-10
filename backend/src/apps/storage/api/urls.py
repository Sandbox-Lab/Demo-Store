from django.urls import path
from . import views

urlpatterns = [
    path('', views.StorageListAPIView.as_view()),
    path('<pk>', views.StorageRetrieveAPIView.as_view()),
]
