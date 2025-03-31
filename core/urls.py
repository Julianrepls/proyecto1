from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomeView.as_view(), name="home"), # con esta línea de código ya tenemos nuestra primera vista apuntando a views desde el import homeview

    path('blog/', include('blog.urls', namespace='blog')) # aqui vamos a configurar todo lo que en nuestra web tenga /blog/ y con el include vamos a incluir las urls de la carpeta blog 
]
