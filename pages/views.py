from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class SettingsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/settings.html'