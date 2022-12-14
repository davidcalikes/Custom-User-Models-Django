from .models import EnrolledPupil, Passport
from django import forms
from allauth.account.forms import SignupForm


TYPE_CHOICES = (
                    ("pupil", "pupil"),
                    ("parent", "parent"),
                    ("teacher", "teacher"),
                    ("school", "school"),
                    )


class CoreSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CoreSignupForm, self).__init__(*args, **kwargs)
        self.fields["user_type"] = forms.ChoiceField(choices=TYPE_CHOICES,
                                                     label='User Type')


class PupilRecordForm(forms.ModelForm):
    """
    Form for adding an enrolled pupil to records database
    """
    class Meta:
        """
        Form has all required fields from EnrolledPupil model
        """
        model = EnrolledPupil
        fields = ('pupil_first_name', 'pupil_last_name',
                  'school_name', 'teacher_name', 'school_roll_no',
                  'pupil_id', 'school_email', )


class PupilPassportForm(forms.ModelForm):
    """
    Form for creating a pupil passport
    """
    class Meta:
        """
        Form has all required fields from Passport model
        """
        model = Passport
        fields = ('my_name',
                  'my_emergency_contact_one_name',
                  'my_emergency_contact_one_number',
                  'my_emergency_contact_two_name',
                  'my_emergency_contact_two_number',
                  'slug', 'my_date_of_birth', 'my_biography',
                  'my_family', 'my_likes', 'my_dislikes', 'my_strengths',
                  'my_difficulties', 'my_supports', 'my_calming_measures',
                  'my_communication_skills', 'my_other_info',
                  'teacher_id', 'pupil_id',
                  )
