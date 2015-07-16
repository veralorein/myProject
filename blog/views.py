from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
	hel='<h1>Hello World</h1>'
	return HttpResponse(hel)
	
def index(request):
	context_dict = {'title': "It's my blog", 'boldmessage': "I'm bold font from the context"}
	return render(request, 'blog/index.html', context_dict)

# Create your views here.
