from django.shortcuts import render, get_object_or_404
from .models import Todo , Category, Contact
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.




def home_view(request):

    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()











    todos = Todo.objects.all()

    sorgu = request.GET.get('sorgu')

    if sorgu:
        todos = todos.filter(
            Q(title__icontains=sorgu) | Q(sehir__icontains=sorgu),
        ).distinct()
    allcategory= Category.objects.all()

    context = dict(
        todos = todos.filter(is_active=True),
        allcategory=allcategory,
    )


    return render(request,'page/index.html',context)



def post_detail(request,id):
    todo = get_object_or_404(Todo,pk=id)
    context= dict(
        todo=todo
    )
    return render(request,"page/post_detail.html",context)




def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    todos = Todo.objects.filter(
        is_active=True,
        category=category,
    )
    context = dict(
        todos = todos,
        category = category,
    )
    return render(request,'page/search_kat.html',context)


