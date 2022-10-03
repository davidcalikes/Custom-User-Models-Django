from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import EnrolledPupil
from .forms import PupilRecordForm


class HomePage(generic.TemplateView):
    """
    Displays instructional video and links on landing page
    """

    template_name = 'index.html'


class EnrolledPupilList(generic.ListView):
    """
    Displays page that lists pupil records created by logged in user
    """
    model = EnrolledPupil
    template_name = 'school_admin.html'
    context_object_name = 'enrolled_pupil_list'

    def get_queryset(self):
        return EnrolledPupil.objects.filter(
            created_by=self.request.user
        )
