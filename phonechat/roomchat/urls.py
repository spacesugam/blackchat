from roomchat import views
from django.urls import path

urlpatterns = [
    path('', views.page,name="secapp"),
    path('next/', views.next_page,name="next_page")
]
