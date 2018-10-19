from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Post

# Create your views here.

def post_home(request): #list of posts Homepage
	queryset = Post.objects.all()
	context = {'object_list': queryset,}

	# if request.user.is_authenticated:
	# 	context = {
	# 		'title': 'User is authenticated',
	# 		'content': 'User is authenticated',
	# 	}

	# else:
	# 	context = {
	# 		'title': 'User is unauthenticated',
	# 		'content': 'User is unauthenticated',
	# 	}

	return render(request,'index.html',context)

def post_create(request):
	return HttpResponse('<h1>Create</h1>')

def post_read(request): #each post
	# instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=2)
	context = {
		'instance': instance,
	}

	return render(request, 'each_post.html', context)

def post_update(request):
	return HttpResponse('<h1>Update</h1>')

def post_delete(request):
	return HttpResponse('<h1>Delete</h1>')
