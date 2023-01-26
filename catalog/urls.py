from django.urls import path
from . import views
from mashupdstack import urls

urlpatterns = [
    
    path('simpleapi/',views.simpleapi,name='simple_api'),
    path('login', views.login, name='login_api'),
    path('medicinedetails/',views.medicinedetails,name='medicinedetails_api'),
    path("create/", views.CreateAPIView.as_view(),name="todo_create"),
    path("update/<int:id>/",views.UpdateAPIView.as_view(),name="update_todo"),
    path("delete/<int:id>/",views.DeleteAPIView.as_view(),name="delete_todo")
    


    
    

]