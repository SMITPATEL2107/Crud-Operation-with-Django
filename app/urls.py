from django.urls import path,include
from . import views
urlpatterns = [
    
    path("",views.IndexPage,name="index"),
    path("insert/",views.Insert,name="insert"),
    path("show/",views.AllData,name="show"),
    path("editpage/<int:pk>",views.getById,name="editpage"),
    path("update/<int:pk>",views.Update,name="update"),
    path("delete/<int:pk>",views.Delete,name="delete")

]