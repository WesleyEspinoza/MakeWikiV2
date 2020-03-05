from django.shortcuts import render
from django.views import generic


from wiki.models import Page


class RegisterView(generic.CreateView):
    form_class = 'django.auth.forms.UserCreationForm'

    def get(self, request):
        return render(request, 'registration/signup.html')
