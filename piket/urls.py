from django.urls import path
from . import views

urlpatterns = [
   
   
    path('', views.berandapiket, name='berandapiket'),
    path('kelola-gaji', views.kelolagaji, name='kelolagaji'),
    path('simpankelolagaji', views.simpankelolagaji, name='simpankelolagaji'),
    
    path('gaji-piket', views.gajipiket, name='gajipiket'),
    
    path('detail-gaji-piket/<str:th>/<str:guru>/<str:bulan>', views.detailgajipiket, name='detailgajipiket'),
    
    
    path('edit-detail-gaji-piket/<str:pk>', views.editdetailgajipiket, name='editdetailgajipiket'),
    path('delete-detail-gaji-piket/<str:pk>', views.deletedetailgajipiket, name='deletedetailgajipiket'),
]

    
