from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
	resources_list = Resource.objects.all()
	paginator = Paginator(resources_list, 24)
	page = request.GET.get('page')

	try:
		resources = paginator.page(page)
	except PageNotAnInteger:
		resources = paginator.page(1)
	except EmptyPage:
		resources = paginator.page(paginator.num_pages)
	return render(request, 'index.html', {'resources' : resources})
