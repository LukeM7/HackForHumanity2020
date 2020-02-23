from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from portfolio.models import Project, ContactInfo


class HomeView(TemplateView):
    template_name = "portfolio/home.html"

class AboutView(TemplateView):
    template_name = "portfolio/about.html"

class ProjectListView(ListView):
    model = Project

    context_object_name = "project_list"
    template_name = "portfolio/project_list_view.html"
    ordering = ['-start_date']


class ProjectDetailView(DetailView):
    model = Project

    context_object_name = "project"
    template_name = "portfolio/project_detail_view.html"


class ContactInfoView(View):

    def get(self, request, *args, **kwargs):
        contact_info = get_object_or_404(ContactInfo, pk=2)
        context = {'contact_info': contact_info}
        return render(request, "portfolio/contact.html", context)
