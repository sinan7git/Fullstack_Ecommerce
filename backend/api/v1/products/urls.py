from django.urls import path
from api.v1.products import views


urlpatterns = [
    path('', views.products),
    path("add_cart/<int:pk>",views.add_to_cart),
    path('view/<int:pk>', views.product),
    path("cart/",views.add_cart),
    path('delete_cart/<int:pk>/', views.delete_cart_item),
]
