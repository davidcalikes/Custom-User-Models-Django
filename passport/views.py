from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import EnrolledPupil, Passport
from .forms import PupilRecordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.template.defaultfilters import slugify


class HomePage(generic.TemplateView):
    """
    Displays instructional video and links on landing page
    """

    template_name = 'index.html'


class EnrolledPupilList(LoginRequiredMixin, generic.ListView):
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


class AddPupilRecord(LoginRequiredMixin, generic.CreateView):
    """
    User with role of School Admin can add an enrolled pupil to database.
    """
    model = EnrolledPupil
    form_class = PupilRecordForm
    template_name = 'pupil_record_form.html'
    success_url = '/'

    def form_valid(self, form):
        """
        Auto applies foreign key and auto generated settings.
        """
        form.instance.created_by = self.request.user
        return super(AddPupilRecord, self).form_valid(form)


class EnrolledPupilRecord(LoginRequiredMixin, View):
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


class UpdatePupilRecord(LoginRequiredMixin, generic.edit.UpdateView):
    """
    User with role of School Admin can update enrolled existing pupil record
    """
    model = EnrolledPupil
    form_class = PupilRecordForm
    template_name = 'pupil_record_form.html'
    success_url = reverse_lazy('enrolled_pupil_list')


class DeletePupilRecord(LoginRequiredMixin, generic.DeleteView):
    """
    User with role of School Admin can delete existing pupil record
    """
    model = EnrolledPupil
    success_url = reverse_lazy('enrolled_pupil_list')

    def delete(self, request, *args, **kwargs):
        return super(DeletePupilRecord, self).delete(request, *args, **kwargs)


class PassportList(LoginRequiredMixin, generic.ListView):
    """
    Displays page that lists pupil records created by logged in user
    """
    model = Passport
    template_name = 'passport_list.html'
    context_object_name = 'passport_list'

    def get_queryset(self):
        return Passport.objects.filter(
            created_by=self.request.user
        )


class PassportDetail(LoginRequiredMixin, View):
    """
    Displays pupil record selected by authenticated user
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Gets selected pupil record
        """
        queryset = Passport.objects.all()
        passport = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'passport_detail.html',
            {
                "passport": passport,
            },
        )


class TeacherPassportList(generic.ListView):
    template_name = 'teacher_passport_list.html'
    model = Passport

    def get_queryset(self):
        query = self.request.GET.get('teacher_id')
        if query:
            object_list = self.model.objects.filter(pupil_id__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class TeacherPassportDetail(LoginRequiredMixin, View):
    """
    Displays pupil record selected by authenticated user
    """
    def get(self, request, teacher_id, *args, **kwargs):
        """
        Gets selected pupil record
        """
        queryset = Passport.objects.all()
        passport = get_object_or_404(queryset, teacher_id=teacher_id)

        return render(
            request,
            'teacher_passport_detail.html',
            {
                "passport": passport,
            },
        )


def LoginSuccess(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.user_type == "school":
        return redirect('enrolled_pupil_list')
    elif request.user.user_type == 'parent':
        return redirect('passport_list')
    elif request.user.user_type == 'teacher':
        return redirect('teacher_passport_list')
    else:
        return redirect('home')
