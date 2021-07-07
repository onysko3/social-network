from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .forms import UserChangeForm, ProfileChangeForm

User = get_user_model()


@login_required
def profile_update(request):
    profile = get_object_or_404(User, username=request.user.username)
    form = ProfileChangeForm(request.POST or None, request.FILES or None, instance=profile)

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
    model = User
    queryset = User.objects.all()
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'


class ProfileListView(ListView):
    model = User
    context_object_name = 'profile_list'
    template_name = 'profiles/profile_list.html'

    def get_queryset(self):
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
            return User.objects.filter(
               Q(first_name__icontains=query) | Q(last_name__icontains=query)
            )
        else:
            return User.objects.all()

