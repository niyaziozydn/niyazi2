from django.shortcuts import render, get_object_or_404
from .models import Todo , Category, Contact
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
import folium

def postaview(request):
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

    sorgu_posta = request.GET.get('sorgu_posta')
    if sorgu_posta:
        todos = todos.filter(
            Q(posta__icontains=sorgu_posta),  # icontains içinde geçen contains direk eşit olan 
        ).distinct()
    else:
        paginator=Paginator(todos,8)

        page_num=request.GET.get('page',1)
        todos=paginator.page(page_num)

    context = dict(
        todos = todos,
       
    )
    return render(request,'page/search_types/postakod.html',context)



def eczaneview(request):
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
    
    todos = Todo.objects.filter(category=Category.objects.get(title="Eczane"))

    sorgu_cezane = request.GET.get('sorgu_eczane')
    if sorgu_cezane:
        todos = todos.filter(
            Q(title__icontains=sorgu_cezane),  # icontains içinde geçen contains direk eşit olan 
        ).distinct()
    else:
        paginator=Paginator(todos,8)

        page_num=request.GET.get('page',1)
        todos=paginator.page(page_num)

    context = dict(
        todos = todos,
       
    )
    return render(request,'page/search_types/eczane.html',context)

def countrykonum_view(request):
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

    sorgu_konum = request.GET.get('sorgu_konum')
    if sorgu_konum:
        todos = todos.filter(
            Q(ulke__icontains=sorgu_konum) | Q(sehir__icontains=sorgu_konum),  # icontains içinde geçen contains direk eşit olan 
        ).distinct()
    else:
        paginator=Paginator(todos,8)

        page_num=request.GET.get('page',1)
        todos=paginator.page(page_num)

    context = dict(
        todos = todos,
       
    )
    return render(request,'page/search_types/countrykonum.html',context)

def phonesearch_view(request):
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

    sorgu_phone = request.GET.get('sorgu_phone')
    if sorgu_phone:
        todos = todos.filter(
            Q(phone__icontains=sorgu_phone),  # icontains içinde geçen contains direk eşit olan 
        ).distinct()
    else:
        paginator=Paginator(todos,8)

        page_num=request.GET.get('page',1)
        todos=paginator.page(page_num)

    context = dict(
        todos = todos,
       
    )
    return render(request,'page/search_types/searchphone.html',context)
