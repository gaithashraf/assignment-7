
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookList.as_view(), name="homepage"),
    path('create/', views.BookCreate.as_view(), name = "addbook"),
    path('delete/<int:pk>', views.BookDelete.as_view(), name = "deletebook"),
    path('update/<int:pk>', views.BookUpdate.as_view(), name="updatebook"),

]
