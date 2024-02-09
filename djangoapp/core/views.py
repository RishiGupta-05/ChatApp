from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import SignUpForm
# Create your views here.
def frontpage(request):
    return render(request,'C:/Users/rutka/Desktop/Projects/djangochat_env/djangoapp/core/templates/core/frontpage.html')

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
        
    else:
            form = SignUpForm()

    return render(request, 'C:/Users/rutka/Desktop/Projects/djangochat_env/djangoapp/core/templates/core/signup.html', {'form':form})

    