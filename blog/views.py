# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from blog.models import Category
from django.views.generic import TemplateView

class MyStructure(object):
	"""docstring for """
	pass


def home_page(request):
	hel='<html><title>Blog lists</title>Hello My PythonBlog <br> "You must be joking!" I can hear you say.</html>'
	return HttpResponse(hel)

def index(request):
	c = MyStructure()
	c.company = 'Cool Star'
	c.title = 'Galina Titova Blog'
	c.author_name = 'Jhon Smith'
	c.pub_date = datetime.datetime.now()
	c.article_list = [{'title': "Title1", 'text': "Text1"}, {'title': "Title2", 'text': "Text2"}, {'title': "Title3", 'text': "Text3"}, {'title': "Title4", 'text': "Text4"}]
	c.boldmessage = "Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context"
	c.text = 'Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context Можно использовать “цепочку” фильтров. Вывод одного фильтра используется для другого. {{ text|escape|linebreaks }} обычно применяется для экранирования текста, и замены переноса строки тегами <p>.'
	return render(request, 'blog/index.html', c.__dict__)

#class AboutView(TemplateView):
	#template_name = "about.html"

def categories(request):
		category_list = Category.object.order_by('name')

		context_dict = {'category_list': category_list}
		return render(request, 'blog/cat.html', context_dict)


# Create your views here.
