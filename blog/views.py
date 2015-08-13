# -*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
import datetime
from blog.models import Category, Post, Comment, Page
from django.views.generic import TemplateView
from blog.forms import UserForm, UserProfileForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
import time
from calendar import month_name

class MyStructure(object):
	"""docstring for """
	pass


def home_page(request):
	hel='<html><title>Blog lists</title>Hello My PythonBlog <br> "You must be joking!" I can hear you say.</html>'
	return HttpResponse(hel)

def index(request):
	#c = MyStructure()
	#c.company = 'Cool Star'
	#c.title = 'Galina Titova Blog'
	#c.author_name = 'Jhon Smith'
	#c.pub_date = datetime.datetime.now()
	#c.article_list = [{'title': "Title1", 'text': "Text1"}, {'title': "Title2", 'text': "Text2"}, {'title': "Title3", 'text': "Text3"}, {'title': "Title4", 'text': "Text4"}]
	#c.boldmessage = "Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context"
	#c.text = 'Вы можете изменить значение переменной используя фильтры. Фильтры выглядят таким образом: {{ name|lower }}. Это выведет значение переменной {{ name }} после применения фильтра lower к нему, который преобразует значение в нижний регистр. Используйте символ (|) для применения фильтра. I am bold font from the context Можно использовать “цепочку” фильтров. Вывод одного фильтра используется для другого. {{ text|escape|linebreaks }} обычно применяется для экранирования текста, и замены переноса строки тегами <p>.'
	#return render(request, 'blog/index.html', c.__dict__)

	#posts_list = Post.objects.order_by('title')

	category_list = Category.objects.order_by('name')
	posts = Post.objects.all().order_by("-created")
	paginator = Paginator(posts, 2)
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	context_dict = {'categories_list':category_list, 'posts':posts, 'months':mkmonth_lst(),  'archive':True }
	return render_to_response("blog/index.html", context_dict)

#class AboutView(TemplateView):
	#template_name = "about.html"

def categories(request):
		category_list = Category.objects.order_by('name')

		context_dict = {'category_list': category_list}
		return render(request, 'blog/cat.html', context_dict)

def category(reqeust, categoryslug):
	name = Category.objects.get(slug = categoryslug)
	posts = Post.objects.filter(category = name)
	context = {'posts': posts}
	return render_to_response('blog/singlecategory.html', context)

def view(request, postslug):
	post = Post.objects.get(slug = postslug)
	comments = Comment.objects.filter(post=post)
	context = {'post': post, "comments":comments,"form":CommentForm(), "user":request.user}
	context.update(csrf(request))
	return render_to_response('blog/singlepost.html', context)

def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit = False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print (user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render(request, 'blog/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate (username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/blog/')
			else:
				return HttpResponse("Your Blog account is disabled.")
		else:
			print ("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'blog/login.html', {})

@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/blog/')

def add_comment(request, postslug):
    p = request.POST
    if p["body"]:
        author = request.user
        comment = Comment(post=Post.objects.get(slug=postslug))
        cf = CommentForm(p, instance=comment)

        cf.fields["author"].required = False
        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect('/blog/')

def mkmonth_lst():
    """Make a list of months to show archive links."""

    if not Post.objects.count(): return []

    # set up vars
    year, month = time.localtime()[:2]
    first = Post.objects.order_by("created")[0]
    fyear = first.created.year
    fmonth = first.created.month
    months = []

    # loop over years and months
    for y in range(year, fyear-1, -1):
        start, end = 12, 0
        if y == year: start = month
        if y == fyear: end = fmonth-1

        for m in range(start, end, -1):
            months.append((y, m, month_name[m]))
    return months

def month(request, year, month):
    """Monthly archive."""

    posts = Post.objects.filter(created__year=year, created__month=month)

    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("blog/list.html", dict(posts=posts, user=request.user, months=mkmonth_lst(),  archive=True))

def page(request, pageslug):
    page = Page.objects.get(slug=pageslug)
    context = {'page': page, "user":request.user}
    return render_to_response('blog/page.html', context)

def track_url(request):
    post_id = None
    url = '/blog/'
    if request.method == 'GET':
        if 'post_id' in request.GET:
            post_id = request.GET['post_id']
            try:
                post = Post.objects.get(id=post_id)
                post.views = post.views + 1
                post.save()
                url = post.url
            except:
                pass

    return redirect(url)
# Create your views here.
