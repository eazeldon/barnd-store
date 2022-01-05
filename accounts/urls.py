from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.dashboard, name='dashboard'),

    # -email activation/admin
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # forget passpord
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('resetPassword/', views.resetPassword, name='resetPassword'),
    #- sect23-len106
    path('my_orders/', views.my_orders, name='my_orders'),
    # sect23-len108
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    # sect23-len111
    path('change_password/', views.change_password, name='change_password'),
    # sect23-len112
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),

]
