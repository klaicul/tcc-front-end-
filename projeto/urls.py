"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from aplicacao.views import upload_image, home, add_carrossel, adicionar_eletivas, lista, apagar_eletivas, apagar_tutoria, adicionar_tutoria, lista_tutoria,view_eletivas,add_social_links,mais_sobre,adicionar_maissobre,apagar_maissobre, add_link_eletivas, apagar_link_eletivas, nossa_historia, add_historia, add_news_one, view_news_one, apagar_news_one

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload_image/', upload_image, name='upload_image'),
    path('add_carrossel/', add_carrossel, name='add_carrossel'),
    path('adicionar_eletivas/', adicionar_eletivas, name='adicionar_eletivas'),
    path('lista/', lista, name='lista'),
    path('<int:eletiva_id>eletiva/', apagar_eletivas, name='apagar_eletivas'),
    path('<int:tutoria_id>tutoria/', apagar_tutoria, name='apagar_tutoria'),
    path('adicionar_tutoria/', adicionar_tutoria, name='adicionar_tutoria'),
    path('lista_tutoria/', lista_tutoria, name='lista_tutoria'),
    path('', home, name='home'),
    path('<int:eletiva_id>/', view_eletivas, name='view_eletivas'),
    path('add_social_links/', add_social_links, name='add_social_links'),
    path('mais_sobre/', mais_sobre, name='mais_sobre'),
    path('adicionar_maissobre/', adicionar_maissobre, name='adicionar_maissobre'),
    path('<int:maissobre_id>maissobre/', apagar_maissobre, name='apagar_maissobre'),
    path('add_link_eletivas/', add_link_eletivas, name='add_link_eletivas'),
    path('delete/<int:link_id>/', apagar_link_eletivas, name='apagar_link_eletivas'),
    path('nossa_historia/', nossa_historia, name='nossa_historia'),
    path('add_historia/', add_historia, name='add_historia'),
    path('add_news_one/', add_news_one, name='add_news_one'),
    path('/<int:noticia_id>/', view_news_one, name='view_news_one'),
    path('<int:noticia_id>noticia/', apagar_news_one, name='apagar_news_one'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)