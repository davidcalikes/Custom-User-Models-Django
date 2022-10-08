from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('login_success/', views.LoginSuccess, name='login_success'),
    path('teacher_passport_list/', views.TeacherPassportList.as_view(), name='teacher_passport_list'),
    path('add_pupil_record/', views.AddPupilRecord.as_view(), name='add_pupil_record'),
    path('add_pupil_passport/', views.AddPupilPassport.as_view(), name='add_pupil_passport'),
    path('validate_pupil_id/', views.ValidatePupilId.as_view(), name='validate_pupil_id'),
    path('enrolled_pupil_list/', views.EnrolledPupilList.as_view(), name='enrolled_pupil_list'),
    path('<int:pupil_id>/', views.EnrolledPupilRecord.as_view(), name='enrolled_pupil_record'),
    path('update/<int:pk>', views.UpdatePupilRecord.as_view(), name='update_pupil_record'),
    path('delete/<int:pk>', views.DeletePupilRecord.as_view(), name='delete_pupil_record'),
    path('passport_list/', views.PassportList.as_view(), name='passport_list'),
    path('<slug:slug>/', views.PassportDetail.as_view(), name='passport_detail'),
    path('teacher_passport_detail/<int:teacher_id>', views.TeacherPassportDetail.as_view(), name='teacher_passport_detail'),
    
    path('login_success/', views.LoginSuccess, name='login_success'),
]
