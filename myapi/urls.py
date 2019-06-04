"""mytalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from talk import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'^talk-auth/', include('rest_framework.urls'))
    # path('talk/v1/products/', store.talk_views.ProductList.as_view()),
    # path('talk/v1/products/new', store.talk_views.ProductCreate.as_view()),
    # path('talk/v1/products/<int:id>/',
    #      store.talk_views.ProductRetrieveUpdateDestroy.as_view()),
    # path(
    #     'talk/v1/products/<int:id>/stats',
    #     store.talk_views.ProductStats.as_view(),
    # ),
    path('talk/', views.GetTalks, name='GetTalks'),
    path('talk/<int:pk>', views.GetTalk, name='GetTalk'),
]
