from django.urls import path
from . import views

urlpatterns=[
  path('',views.Person_Create_Detail),
  path('<int:pk>/',views.Person_Detail),
  path('<int:pk>/delete/',views.Person_Delete_Detail),
  path('<int:pk>/update/',views.Person_Update_Detail),
  path('list/',views.Person_List_Detail)
  
  ]