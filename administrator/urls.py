from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.halamanlogin, name='halamanlogin'),
    path('administrator/', views.berandaadmin, name='berandaadmin'),
    path('logout/', views.logoutPage, name='logout'),
    
    path('tahun-pelajaran/', views.tahunpelajaran, name='tahunpelajaran'),
     path('form-tahun-pelajaran/', views.formtahunadmin, name='formtahunadmin'),
    path('edit-tahun-pelajaran/<str:pk>', views.edittahunadmin, name='edittahunadmin'),
    path('delete-tahun-pelajaran/<str:pk>', views.deletetahunadmin, name='deletetahunadmin'),
    
    path('jam-pelajaran/', views.jampelajaran, name='jampelajaran'),
    path('form-jam-pelajaran/', views.formjamadmin, name='formjamadmin'),
    path('edit-jam-pelajaran/<str:pk>', views.editjamadmin, name='editjamadmin'),
    path('delete-jam-pelajaran/<str:pk>', views.deletejamadmin, name='deletejamadmin'),
    
    path('setting-gaji/', views.settinggaji, name='settinggaji'),
    path('form-setting-gaji/', views.formsettinggajiadmin, name='formsettinggajiadmin'),
    path('edit-setting-gaji/<str:pk>', views.editsettinggajiadmin, name='editsettinggajiadmin'),
    path('delete-setting-gaji/<str:pk>', views.deletesettinggajiadmin, name='deletesettinggajiadmin'),
    
    path('piket-admin/', views.piketadmin, name='piketadmin'),
    path('form-piket-admin/', views.formpiketadmin, name='formpiketadmin'),
    path('form-edit-piket-admin/<str:pk>', views.editpiketadmin, name='editpiketadmin'),
    path('delete-piket-admin/<str:pk>', views.deletepiketadmin, name='deletepiketadmin'),
    
    
     path('guru-admin/', views.guruadmin, name='guruadmin'),
    path('form-guru-admin/', views.formguruadmin, name='formguruadmin'),
    path('form-edit-guru-admin/<str:pk>', views.editguruadmin, name='editguruadmin'),
    path('delete-guru-admin/<str:pk>', views.deleteguruadmin, name='deleteguruadmin'),
    
    
     path('gaji-admin/', views.gajiadmin, name='gajiadmin'),
     path('detail-gaji-admin/<str:th>/<str:guru>/<str:bulan>', views.detailgajiadmin, name='detailgajiadmin'),
     
     
     path('edit-detail-gaji-admin/<str:pk>', views.editdetailgajiadmin, name='editdetailgajiadmin'),
    path('delete-detail-gaji-admin/<str:pk>', views.deletedetailgajiadmin, name='deletedetailgajiadmin'),
]