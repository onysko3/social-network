from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Profile
from .forms import ProfileForm


def profile_update(request):
    profile = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)

    success = False

    if form.is_valid():
        form.save()
        success = True

    context = {
        'form': form,
        'success': success
    }

    return render(request, 'profiles/profile_update.html', context)


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profile_list'
    template_name = 'profiles/profile_list.html'

    def get_queryset(self):
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            return Profile.objects.filter(
               Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        else:
            return Profile.objects.all()

