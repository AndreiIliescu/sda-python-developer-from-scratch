from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views import View
from django.shortcuts import redirect


class SubmittableLoginView(LoginView):
    template_name = 'form.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')
