from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from post.models import Post, Tag

def index(request):
	if 'tags' in request.GET:
		posts = Post.objects.filter(tags__tag_name=request.GET['tags'])
	else:
		posts = Post.objects.order_by('-pub_date')
	tags = Tag.objects.order_by('tag_name')
	return render(request, 'mysite/index.html', {'posts': posts, 'tags': tags})

def show(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'mysite/show.html', {'post': post})

def save(request):
	user = None
	
	if request.user.is_authenticated():
		user = request.user
	else:
		return HttpResponseRedirect('/')
	post = Post(post_title=request.POST['post_title'], post_body=request.POST['post_body'], post_author=user, pub_date=timezone.now())
	post.save()
	tags = Tag.objects.get(id=request.POST['tags'])
	post.tags.add(tags)
	return redirect('/')