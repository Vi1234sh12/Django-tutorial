# from django.shortcuts import render
# from django.template import loader
# from django.http import HttpResponse
#
# # def Signup(request):
# #     return HttpResponse("signup page")

# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from mybook.models import Books


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

