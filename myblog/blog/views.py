# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from models import Post, Comment
from django.template import Context, loader, Template
from django.shortcuts import render_to_response
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def post_list(request):
    posts = Post.objects.all()
    t = loader.get_template('blog/post_list.html')
    c = Context({'posts':posts })
    return HttpResponse(t.render(c))

'''def post_list(request):
    post_list = Post.objects.all()
    print type(post_list)
    print post_list
    lis=[]
    for e in post_list:
        lis.append(e.title)
    return HttpResponse(lis)'''

class CommentForm(ModelForm):
  class meta:
    model=Comment

@csrf_exempt

def post_detail(request, id, showComments=False):
    if request.method == 'POST':	
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = CommentForm()

    post=Post.objects.get(pk=id)
    if(showComments):
     out='<h1>'+post.title+'</h1>'+'<br>'+post.body[:100]+'<br>'+post.body[100:200]
    else:
        out=post.title+'\n'
    return HttpResponse(out)

def post_search(request, term):
    pass

def home(request):
    return render_to_response('blog/base.html',{}) 
