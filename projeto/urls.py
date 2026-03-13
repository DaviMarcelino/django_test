from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('teste/',views.teste_view),
    path('tarefas/', include("tarefas.urls"))
]