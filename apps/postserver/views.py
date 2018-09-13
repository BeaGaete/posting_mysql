from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.postserver.forms import PostForm
from apps.postserver.models import Post
from datetime import datetime
# Create your views here.


def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    #return HttpResponse('Hello world ' + ip)
    return render(request, 'postserver/index.html')

def post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.ip = request.META['REMOTE_ADDR']
            #print(profile.ip)
            #profile.timestamp = datetime.now()
            #print(profile.timestamp)
            profile.save()
        return redirect('/nuevo')  # 'postserver:index'
    else:
        form = PostForm()
    return render(request, 'postserver/post_form.html', {'form':form})

def post_list(request):
    posts = Post.objects.order_by('-id')[:5][::-1]
    contexto = {'posts':posts}
    return render(request, 'postserver/postserver_list.html', contexto)
