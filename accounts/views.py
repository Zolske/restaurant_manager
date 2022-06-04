from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


# use Django’s generic CreateView
class SignUpView(CreateView):
    # tell Django to use our CustomUserCreationForm
    form_class = CustomUserCreationForm
    # redirect to login once a user signs up successfully
    success_url = reverse_lazy('login')
    # template is named signup.html
    template_name = "registration/signup.html"