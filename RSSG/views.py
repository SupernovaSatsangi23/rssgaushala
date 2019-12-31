from django.shortcuts import render
from .models import Home, Alpha, About, Gallery, History, Operations

# Create your views here.
def home(request):
	context = {'Home': Home.objects.all()}
	return render(request, 'RSSG/home.html', context)

def alpha(request):
	context = {'Alpha': Alpha.objects.all()}
	return render(request, 'RSSG/alpha.html', context)

def about(request):
	context = {'About': About.objects.all()}
	return render(request, 'RSSG/about.html', context)

def gallery(request):
	context = {'Gallery': Gallery.objects.all()}
	return render(request, 'RSSG/gallery.html', context)

def history(request):
	context = {'History': History.objects.all()}
	return render(request, 'RSSG/history.html', context)

def operations(request):
	context = {'Operations': Operations.objects.all()}
	return render(request, 'RSSG/operations.html', context)

