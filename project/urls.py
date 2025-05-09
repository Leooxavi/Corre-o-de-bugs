from django.contrib import admin
from django.urls import path
from home import views # não estava importando as views do app 'home'

urlpatterns = [
    
    path('produto/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'), 
    path('produto/listar/', views.listar_produto, name='listar_produto'),
    path('admin/', admin.site.urls),
]
