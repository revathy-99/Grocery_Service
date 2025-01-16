from django.urls import path
from . import views

urlpatterns = [
    #path('add', views.addproduct),
    #path('display', views.display),
    #path('delete/<int:pid>',views.delete),
    #path('update', views.updatename),
    path('', views.product_list, name='product_list'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
