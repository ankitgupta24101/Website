"""
URL configuration for MyWebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from django.views.static import serve
from django.http import HttpResponse
import os
from . import views

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

urlpatterns = [
    path('members/', views.members, name='members'),

    path('members/details/<int:id>', views.details, name='details'),
    path('', views.home, name='home'),
    # Serve static files for website and AI
    re_path(r'^(?P<page>website|ai)/(?P<folder>CSS|Image|JavaScript)/(?P<path>.*)$',
            lambda request, page, folder, path: views.serve_static(request, folder, path)),

    # Optional: serve root-level CSS/JS/Image if HTML uses /CSS/... directly
    re_path(r'^(?P<folder>CSS|Image|JavaScript)/(?P<path>.*)$',
            lambda request, folder, path: views.serve_static(request, folder, path)),
    path('website/', views.serve_html, name='website'),
    path('website/<str:html_file>/', views.serve_html, name='website'),
    path('ai/', views.ai_page, name='ai_page'),
    path('ai-input/', views.ai_input, name='ai_input'),  # POST endpoint
]
