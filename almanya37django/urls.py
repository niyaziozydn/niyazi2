"""almanya37django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page.views import home_view,post_detail, category_detail, contact, about_view
from page.searchviews import postaview, eczaneview, countrykonum_view, phonesearch_view

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view, name='home_view'),
  

    path('todo/<int:id>/',post_detail, name='post_detail'),
    path('category/<slug:category_slug>/',category_detail, name='category_detail'),
    path('postsearch/',postaview, name='postaview'),
    path('eczane/',eczaneview, name='eczaneview'),
    path('countrysearch/',countrykonum_view,name='countrykonum_view'),
    path('phonesearch/',phonesearch_view,name='phonesearch_view'),
    path('contact/',contact,name='contact'),
    path('about/',about_view,name="about_view")




  

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)