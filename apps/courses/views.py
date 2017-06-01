from django.shortcuts import render,redirect
from models import Course, Description

def index(request):
	courses = Course.objects.all()
	descriptions = Description.objects.all()
	context = {
	'courses': courses,
	'descriptions': descriptions
	}
	return render(request, 'index.html', context)

def process_add(request):
	name = request.POST['name']
	description = request.POST['description']
	Description.objects.create(description=description)
	des = Description.objects.get(description=description)
	Course.objects.create(name=name, description=des)
	# print Course.objects.all()
	return redirect('/')

def delete(request, id):
	course = Course.objects.get(id = id)
	context = {
	'id': id,
	'name': course.name,
	'description': course.description
	}
	return render(request, 'delete.html', context)