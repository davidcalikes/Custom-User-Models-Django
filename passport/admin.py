from django.contrib import admin
from .models import EnrolledPupil, Passport


@admin.register(EnrolledPupil)
class EnrolledPupilAdmin(admin.ModelAdmin):
    list_display = ('pupil_first_name', 'pupil_last_name',
                    'school_name', 'teacher_name', 'school_roll_no',
                    'pupil_id', 'school_email', 'created_by',
                    'last_updated')
    search_fields = ('pupil_first_name', 'pupil_last_name',
                     'school_name', 'teacher_name', 'school_roll_no',
                     'pupil_id', 'school_email', 'created_by',
                     'last_updated')

    def approved_entry(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    list_display = ('my_name',
                    'my_emergency_contact_one_name', 
                    'my_emergency_contact_one_number', 
                    'my_emergency_contact_two_name', 
                    'my_emergency_contact_two_number',
                    'slug', 'my_date_of_birth', 'my_biography', 
                    'my_family', 'my_likes', 'my_dislikes', 'my_strengths',
                    'my_difficulties', 'my_supports', 'my_calming_measures',
                    'my_communication_skills', 'my_other_info',
                    'created_by',
                    )
    search_fields = ('my_name',
                     'my_emergency_contact_one_name', 
                     'my_emergency_contact_one_number', 
                     'my_emergency_contact_two_name', 
                     'my_emergency_contact_two_number',
                     'slug', 'my_date_of_birth', 'my_biography', 
                     'my_family', 'my_likes', 'my_dislikes', 'my_strengths',
                     'my_difficulties', 'my_supports', 'my_calming_measures',
                     'my_communication_skills', 'my_other_info',
                     'created_by',
                     )

    def approved_entry(self, request, queryset):
        queryset.update(approved=True)
