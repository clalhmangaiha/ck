from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post,Comment,Bookmark,Activity,Category
from .forms import PostForm,EditPostForm
from django.db.models import Q
from django.contrib.auth.models import User
# from django.contrib.auth.admin import 
# Create your views here.

def index(request):
    posts = Post.objects.all()
    # posts = "HELLO"
    # return HttpResponse("A tha vek e aw.")
    context ={'posts':posts}
    return render(request,'ed/index.html',context)
        
def categories(request,id):
    if id == 28:
        categories = Category.objects.all()
        return render(request,'ed/category/categories_index.html',{'categories':categories})
      
    else:
        categories = Category.objects.get(id=id)
        posts = Post.objects.filter(category=categories)
        return render(request,'ed/category/categories.html',{'posts':posts,'categories':categories})

def details(request,id):
    details = get_object_or_404(Post,id=id)
    comments = Comment.objects.filter(post=details)
    related = details.tags.similar_objects()[:3]

    def get_ip(request):
        address = request.META.get('HTTP_X_FORWARDED_FOR')
        if address:
            ip = address.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip = get_ip(request)
  

    u = Activity(post=details,user=ip)
    result = Activity.objects.filter(post=details,user__contains=ip)
    if len(result) == 1:
        print("IP ADDRESS FOUND",ip)
    else:
        u.save()
        print("UNIQUE")
    counter = Activity.objects.filter(post=details).count()
    if request.user.is_authenticated:
        bookmarked = Bookmark.objects.filter(user=request.user,post=details)
        return render(request,'ed/details.html',{'details':details,'related':related,'comments':comments,'counter':counter,'bookmarked':bookmarked})
    else:
        return render(request,'ed/details.html',{'details':details,'related':related,'comments':comments,'counter':counter,})

def postform(request):
    user = request.user
  
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.Author = request.user
            try:
                f.save()
                form.save_m2m()
                return redirect('/')
            except:
                pass
                return redirect('/')
        
    else:
        form = PostForm()
    return render(request,'ed/postform.html',{'form':form,})
        
def edit(request,id):
    post = get_object_or_404(Post,id=id)
    category = Category.objects.all()
    form = EditPostForm(request.POST or None,request.FILES or None,instance=post)
    t = [i.name for i in post.tags.all()]
    t =",".join(t)
    context={'form':form,'post':post,'t':t,'category':category}
    detail_url =f'/{id}'
    if form.is_valid():
        
        obj = form.save(commit=False)
       
        if obj.Author == request.user:
            # post.tags.add(request.POST.get('tags'))
            # post.save()
            # print("HI" ,post.tags)
            obj.save()
            form.save_m2m()
            print("DONE")
        
            return redirect(detail_url)
    return render(request,'ed/edit.html',context)



def delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/')

def comment(request,id):
    
    p = Post.objects.get(id=id)
    y =request.POST.get('comment')
    post = Comment(post=p,commenter = request.user,comment= y)
    # post.comment = request.POST.get('comment')odelodel
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def editcomment(request,id):
    com = get_object_or_404(Comment,id=id)
    com.comment = request.POST.get('comment')
    com.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def deletecomment(request,id):
    com = get_object_or_404(Comment,id=id)
  
    com.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def bookmark(request,id):
    b,created = Bookmark.objects.get_or_create(user=request.user)
    post = get_object_or_404(Post,id=id)
 
    if post in b.post.all():  
        b.post.remove(post)
        b.save()
    else:
        b.post.add(post)
        b.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    
    query= request.GET.get("query")
    post_results = Post.objects.filter(title__icontains=query)
    user_results = User.objects.filter(username__icontains=query)
    category_results = Category.objects.filter(name__icontains=query)
    return render(request,'ed/search/search.html',{'post_results':post_results,'user_results':user_results,'category_results':category_results})