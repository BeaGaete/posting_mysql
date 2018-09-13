from django.urls import path

from apps.postserver.views import index, post_view, post_list

urlpatterns = [
    path('', index, name='index'),
    path('nuevo', post_view, name='postserver'),
    path('listar', post_list, name='postserver'),
]
