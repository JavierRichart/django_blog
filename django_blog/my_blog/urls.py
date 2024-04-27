from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_post, name='lista_posts'),
    path('post/<int:post_id>/', views.detalle_post, name='detalle_post'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categoria/<int:categoria_id>/', views.posts_por_categoria, name='posts_por_categoria')
]