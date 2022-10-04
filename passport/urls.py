from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('enrolled_pupil_list/', views.EnrolledPupilList.as_view(), name='enrolled_pupil_list'),
    path('add_pupil_record/', views.AddPupilRecord.as_view(), name='add_pupil_record'),
    path('<int:pupil_id>/', views.EnrolledPupilRecord.as_view(), name='enrolled_pupil_record'),
]
