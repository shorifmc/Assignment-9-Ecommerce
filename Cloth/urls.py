from django.urls import path
from . import views

urlpatterns = [
    path('',views.cloth),
    path('shirt/',views.getShirt),
    path('pant/',views.getPant),
    path('tshirt/',views.getTshirt),

    

]

