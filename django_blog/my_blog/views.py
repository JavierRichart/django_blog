from django.shortcuts import render, get_object_or_404
from .models import Categoria, Post

def lista_post(request):
    posts = Post.objects.all()
    if not posts:
        mensaje = "No hay posts disponibles en este momento"
    else:
        mensaje= None
    return render(request, 'my_blog/lista_posts.html', {'posts': posts, 'mensaje': mensaje})

def detalle_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'my_blog/detalle_post.html', {'post': post})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'my_blog/lista_categorias.html', {'categorias': categorias})

def posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    return render(request, 'my_blog/posts_por_categoria.html', {'categoria': categoria, 'posts': posts})