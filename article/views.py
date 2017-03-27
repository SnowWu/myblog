# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
#from django.utils.timezone import utc
#utcnow = datetime.utcnow().replace(tzinfo=utc)
# Create your views here.
'''def home(request):
	return HttpResponse("Hello World, Django")'''

'''def detail(request, my_args):
	post = Article.objects.all()[int(my_args)]
	str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))
	return HttpResponse(str)'''

'''def test(request):
	return render(request, 'test.html', {'current_time': datetime.now()})'''

def home(request):
	post_list = Article.objects.all()
	return render(request, 'home.html', {'post_list' : post_list})  #'current_time':utcnow

def detail(request, id):
	try:
		post = Article.objects.get(id = str(id))
		post.content = custom_markdown(post.content)
	except Article.DoesNotExist:
		raise django.http.Http404
	return render(request, 'post.html', {'post' : post})
