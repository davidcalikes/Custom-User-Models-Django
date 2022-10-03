from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('enrolled_pupil_list/', views.EnrolledPupilList.as_view(), name='enrolled_pupil_list'),
]
