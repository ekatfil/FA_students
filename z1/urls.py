"""
URL configuration for z1 project.

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
from django.contrib import admin
import main.views as main
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main.index, name="index"),
    path("table/", main.table, name="table"),
    path('add_table/', main.add_table, name='add_table'),
    path('edit_table/<int:table_id>/', main.edit_table, name='edit_table'),
    path('delete_table/<int:table_id>/', main.delete_table, name='delete_table'),
    path("about/", main.about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
