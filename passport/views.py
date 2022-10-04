from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import EnrolledPupil
from .forms import PupilRecordForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify


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


class EnrolledPupilRecord(View):
    """
    Displays pupil record selected by authenticated user
    """
    def get(self, request, pupil_id, *args, **kwargs):
        """
        Gets selected pupil record
        """
        queryset = EnrolledPupil.objects.all()
        record = get_object_or_404(queryset, pupil_id=pupil_id)

        return render(
            request,
            'pupil_record.html',
            {
                "record": record,
            },
        )


class AddPupilRecord(generic.CreateView):
    """
    User with role of School Admin can add an enrolled pupil to database.
    """
    model = EnrolledPupil
    form_class = PupilRecordForm
    template_name = 'add_pupil_form.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        return super(AddPupilRecord, self).form_valid(form)
