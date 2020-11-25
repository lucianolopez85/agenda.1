from django.urls import path
from . import views

urlpatterns = [
    path('', views.metodo_index, name='index'),
    path('<int:contato_detalhe_id>', views.metodo_detalhe, name='detail'),

]