from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from .models import *
from .forms import *
pusher = Pusher(app_id=u'295876', key=u'4b34c484eeb9fe4f4142', secret=u'6b17e2a894fc39296783')

@login_required(login_url='/admin/login/')
def chat(request):
    return render(request,"chat.html");


@csrf_exempt
def broadcast(request):
    
    pusher.trigger(u'a_channel', u'an_event', {u'name': request.user.username, u'message': request.POST['message']})
    return HttpResponse("done");
    
def index(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
    return render(request,'home.html',context)

def index1(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
        #taco
    return render(request,'Overwatch.html',context)
def index2(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
    return render(request,'TeamFortress2.html',context)
def index3(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
    return render(request,'Dota2.html',context)
def index4(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
    return render(request,'CallofDutyWW2.html',context)
def index5(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
    return render(request,'Fortnite.html',context)
def index6(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            submit = form.cleaned_data['comment']
            newComment = Comment(comment=submit)
            newComment.save()
            form = CommentForm()
        else:
            submit = ""
    else:
        form = CommentForm()
        submit = ""
    comments = Comment.objects.all()
    context = {
        'title':"Home",
        'content': comments,
        'form':form,
        'submit':submit
        }
    return render(request,'chat.html',context)