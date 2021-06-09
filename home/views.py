from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
from  django.contrib.auth import login, logout, authenticate
from blog.models import Post
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    #showing Warning/success msg
    #messages.success(request, 'Welcome To Contact')
    #set the parameter
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        print('name','email', 'msg')
        # creating Arguement for saving the data in the database
        if len(phone) < 11 :
            messages.error(request, 'Please Input Correct Phone Number')
        else:
            contact = Contact(name=name, email=email, phone=phone, msg=msg)
            #save data
            contact.save()
            messages.success(request, 'Thanks For Contacting, We will get back to you soon! 💖')

       
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')


def search(request):
    query =request.GET['query']
    if len(query)>78:
        allPosts = Post.objects.none()
    else:
        allPostst = Post.objects.filter(post_title__icontains=query)
        allPostsc = Post.objects.filter(content__icontains=query)
        allPostsa = Post.objects.filter(author__icontains=query)
        allPostx = allPostst.union(allPostsc)
        allPosts = allPostsa.union(allPostx)
    if allPosts.count() == 0:
         messages.warning(request, 'No Search Results Found')

    params = {'allPosts': allPosts, 'query':query}

    return render(request, 'home/search.html', params)




def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) >10:
            messages.error(request,"Your Username must be under 10 characters")
            return redirect ("/")
        if not username.isalnum():
            messages.error(request,"Username must be Alphanumeric")
            return redirect ("/")
        if pass1 != pass2:
            messages.error(request,"Your Password is not Same")
            return redirect ("/")
        
        myuser =  User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,'Your Account has been successfully created')
        return redirect('/')
    else:
        return HttpResponse('404 Not Found')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername , password=loginpass)

        if user is not None:
            login(request, user)
            messages.success(request, "You Are Successfully Logged In ")
            return redirect ("/")
        else:
            messages.error(request, "Invalid Credentials, Please Try Again")

    return HttpResponse('404 Not Found')


def handlelogout(request):
    logout(request)
    messages.success(request,'You are successfully logout')
    return redirect ("/")
    



