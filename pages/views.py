from django.shortcuts import render
from pages.forms import RegisterForm
from users.models import User

# Create your views here.
def pages_home_view(request):
	context = {}
	return render(request, 'pages_home.html', context)

def pages_login_view(request):
	print(f'GET - {request.GET}')
	print(f'POST - {request.POST}')
	context = {}
	return render(request, 'pages_login.html', context)

def pages_register_view(request):
	form = RegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = RegisterForm
	context = {
		'form': form,
	}
	return render(request, 'pages_register.html', context)
