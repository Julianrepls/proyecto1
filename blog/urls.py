from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name="blog"

#con esto podemos acceder a todas nuestras vistas por crear de la carpega blog
urlpatterns = [
    path('Bienvenido/', BlogListView.as_view(), name="home"), # al poner ese bienvenido/ entre las comillas cuand yo en mi pagina de inicio pinche en el boton "aqui" va aparecer en mi url esto: http://127.0.0.1:8000/blog/Bienvenido/    Ese bienvenido/
    path('create/', BlogCreateView.as_view(), name="create"),
    path('<int:pk>/', BlogDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete")

]