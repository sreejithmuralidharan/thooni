from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model       =       Profile
    template_name   =   'accounts/profile_detail.html'