from django.shortcuts import render, get_object_or_404
from .models import Todo , Category, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import folium



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
        messages.success(request, "Form Başariyla Gönderildi")
        return redirect('home_view')
    todos = Todo.objects.all()
 
    
        



    sorgu = request.GET.get('sorgu')
    if sorgu:
        todos = todos.filter(
            Q(category__title__icontains=sorgu) | Q(sehir__icontains=sorgu),  # icontains içinde geçen contains direk eşit olan 
        ).distinct()
    else:
        paginator=Paginator(todos,8)
        page_num=request.GET.get('page',1)
        todos=paginator.page(page_num)
    allcategory= Category.objects.all()

    
    

    
   

    context = dict(
        todos = todos,
        allcategory=allcategory,
       
    )


    return render(request,'page/index.html',context)



def post_detail(request,id):
    todo = get_object_or_404(Todo,pk=id)
    lat = 40.7128  # Örnek bir enlem değeri (New York City)
    lon = -74.0060  # Örnek bir boylam değeri (New York City)
    map = folium.Map(location=[lat, lon], zoom_start=12)
    folium.Marker([lat, lon], popup='Sample Location').add_to(map)

    context= dict(
        todo=todo,
        
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



def contact(request):
    
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        messages.success(request, "Form Başariyla Gönderildi")
        return redirect('home_view')
    
    return render(request,'page/contactpage.html')


def about_view(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        messages.success(request, "Form Başariyla Gönderildi")
        return redirect('home_view')
    return render(request,'page/about.html')
