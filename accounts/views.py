from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from guardian.mixins import PermissionRequiredMixin, PermissionListMixin
from .models import Profile
from .forms import ProfileForm, SignUpForm


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model       =       Profile
    template_name = 'accounts/profile_detail.html'

class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    model       =       Profile
    form_class  =       ProfileForm
    permission_required = ['view_profile', 'change_profile']
    template_name   =   'base/snippets/forms/create_update.html'


class SignupCreateView(CreateView):
    form_class      =   SignUpForm
    template_name   =   'accounts/signup.html'
    def form_valid(self, form):
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(self.request, user)
            user_id = user.id
            return redirect(reverse('accounts:profile-update', args= { user_id}))
        return render(self.request, reverse('accounts:signup'), {'form': form})    