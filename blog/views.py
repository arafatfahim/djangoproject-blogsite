from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, Blogpostcomment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras

# Create your views here.

def index(request):
    allPosts = Post.objects.all()
    #print(allPosts)
    context = {'allPosts': allPosts}
    return render(request, 'blog/home.html', context)

def blogpost(request, slug):

    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    comments = Blogpostcomment.objects.filter(post=post, parent=None)
    replies = Blogpostcomment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.com_id not in repDict.keys():
            repDict[reply.parent.com_id] =[reply]
        else:
            repDict[reply.parent.com_id].append(reply)
    context = {'post' : post, 'comments':comments, 'user' : request.user, 'repDict' : repDict}
    #if request.method == 'POST':
     #   post_title = request.POST['post_title']
      #  author = request.POST['author']
     #   content = request.POST['content']

      #  post = Post(post_title=post_title, author=author, content=content)
      #  post.save()


    return render(request, 'blog/blogpost.html', context)

def Postcomment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(post_id=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == "":
            comment = Blogpostcomment(comment=comment, user=user, post=post)
            messages.success(request, 'Your comment hasbeen successfully')
        else:
            parent = Blogpostcomment.objects.get(com_id=parentSno)
            comment = Blogpostcomment(comment=comment, user=user, post=post, parent=parent)
            messages.success(request, 'Your reply hasbeen successfully')
            
            
        comment.save()
    return redirect(f"/blog/{post.slug}")

