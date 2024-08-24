from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.berandaguru, name='berandaguru'),
    
    path('gaji-guru', views.gajiguru, name='gajiguru'),
    
    path('detail-gaji-guru/<str:th>/<str:guru>/<str:bulan>', views.detailgajiguru, name='detailgajiguru'),

    
]