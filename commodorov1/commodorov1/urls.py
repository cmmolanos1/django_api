"""commodorov1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from places.views import *
from products.views import *
from users.views import *
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/farms/$', FarmsListView.as_view()),
	url(r'^api/v1/farms/(?P<pk>\d+)/$', FarmsView.as_view()),
	url(r'^api/v1/pictures/$', PicturesListView.as_view()),
	url(r'^api/v1/pictures/(?P<pk>\d+)/$', PicturesView.as_view()),
	url(r'^api/v1/coffees/$', CoffeesListView.as_view()),
	url(r'^api/v1/coffees/(?P<pk>\d+)/$', CoffeesView.as_view()),
	url(r'^api/v1/users/$', UsersListView.as_view()),
	url(r'^api/v1/users/(?P<pk>\d+)/$', UsersView.as_view()),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)