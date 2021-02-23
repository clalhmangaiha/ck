from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import Profile,Follower
from django.contrib.auth.views import LoginView
from blog.models import Bookmark,Post
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create your views here.


def user_index(request):
    users = Profile.objects.all()
    return render(request,'User/user_index.html',{'users':users})

def user_detail(request,u):
    user = User.objects.get(username=u)
    profile = get_object_or_404(Profile,name=user.id)
    posts = Post.objects.filter(Author=profile.name)
    followers = Follower.objects.filter(following=user)
    following = Follower.objects.filter(follower=user).count()
    if request.user.is_authenticated:
        follow_status = Follower.objects.filter(follower=request.user,following=user)
        return render(request,'User/user_detail.html',{'profile':profile,'posts':posts,'followers':followers,
        'following':following,'follow_status':follow_status})
    else:
        return render(request,'User/user_detail.html',{'profile':profile,'posts':posts,'followers':followers,
        'following':following,})


class Login(LoginView):
    template_name = 'Registration/login.html'

def logout_view(request):
    logout(request)
    return redirect('/')

def follow(request,id):
    follower = request.user
    following = User.objects.get(id=id)
    print(follower,id)
    f = Follower(follower=follower,following=following)

    if Follower.objects.filter(follower=follower,following=following):
        f = Follower.objects.get(follower=follower,following=following)
        f.delete()
    else:
        f.save()
       
        
        
    # except Follower.objects.get(follower=follower,following=following).DoesNotExist:
        
    #     f = Follower(follower=follower,following=following)
    #     f.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def me(request):
    if request.user is True:
        user = request.user
        profile = Profile.objects.get(name=user)
        bookmarks = Bookmark.objects.get(user=user)
        posts = Post.objects.filter(Author=user)
        following = Follower.objects.filter(follower=user)
        followers = Follower.objects.filter(following=user)

        return render(request,'Dashboard/myprofile.html',{'profile':profile,'bookmarks':bookmarks,'posts':posts,'following':following,'followers':followers})

    else:
        return redirect('/users/accounts/login')
