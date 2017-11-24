from django.shortcuts import render
from django.http import HttpResponse
from .models import Resource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
	resources_list = Resource.objects.all().order_by('?')
	paginator = Paginator(resources_list, 40)
	page = request.GET.get('page')

	try:
		resources = paginator.page(page)
	except PageNotAnInteger:
		resources = paginator.page(1)
	except EmptyPage:
		resources = paginator.page(paginator.num_pages)
	return render(request, 'index.html', {'resources' : resources})

def detail(request, resource_id):
	resource = Resource.objects.get(id=resource_id)
	return render(request, 'detail.html', {'resource' : resource})
