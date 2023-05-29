from django.urls import path
from labapp import views

urlpatterns = [
   path('main',views.main),
   path('delete/<rid>',views.delete),
   path('edit/<rid>',views.edit),
   path('bill/<rid>',views.bill),
   path('fbill/<rid>',views.fbill),
   
]
