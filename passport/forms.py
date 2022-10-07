from .models import EnrolledPupil
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
