from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login
from django.contrib import messages

from .forms import NewUserForm

class RegisterView(View):
    def get(self, request):
        form = NewUserForm()
        return render(
            request=request, 
            template_name="registration/register.html", 
            context={"register_form":form}
        )

    def post(self, request):
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
        return render(
            request=request, 
            template_name="registration/register.html", 
            context={"register_form":form}
        )