from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'createaccount.html'
    success_url= reverse_lazy('login')

    # def userprofile(self, request): 
    #     user = users.objects.all()
    #     pictures # = model, get_object for current user = request.user
    #     return (request, self.template_name, )

class UserProfileView(DetailView):
    model = User
    template_name = 'userprofile.html'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

