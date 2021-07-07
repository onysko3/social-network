from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    def get_template_names(self):
        if self.request.user.is_authenticated:
            return redirect('post_list')
        return 'pages/home.html'


class SettingsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/settings.html'