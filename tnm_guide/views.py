from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource


# Create your views here.
def index(request):
	resources = Resource.objects.all()
	return render(request, 'index.html', {'resources' : resources})

