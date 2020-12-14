from django.contrib import admin
from django.urls import path, include
from app_blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="url_home"),
    path('editsamplepostblog/<int:id>/', views.editsamplepostblog, name="url_editsamplepostblog"),
    path('editdestaquepostblog/<int:id>/', views.editdestaquepostblog, name="url_editdestaquepostblog"),
    path('deletardestaque/<int:id>/', views.deletardestaque, name="url_deletardestaque"),
    path('deletarsample/<int:id>/', views.deletarsample, name="url_deletarsample"),
    path('newsamplepostblog/', views.newsamplepostblog, name="url_newsamplepostblog"),
    path('newdestaquepostblog/', views.newdestaquepostblog, name="url_newdestaquepostblog"),
    path('accounts/', include('app_accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
