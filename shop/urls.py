from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path('prodview/<int:myid>', views.prodview, name='ProductView'),
    path('checkout/', views.checkout, name='Checkout'),
    path('tracker/', views.tracker, name='TrackingStatus'),
    path('handlerequest/', views.handlerequest, name='HandleRequest'),
]
