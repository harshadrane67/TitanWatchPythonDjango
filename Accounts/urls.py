from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as account_views

urlpatterns = [
    path('register/', account_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="Accounts/login.html"), name='login'),
    path('logout/', account_views.logout, name='logout'),
    path('profile/', account_views.profile, name='profile'),
    path('profile/update', account_views.profile_update, name='profile-update'),
    path('profile/address', account_views.address, name='profile-address'),
    path('profile/address/form/', account_views.address_from, name='profile-address-form'),
    path('profile/address/update/<int:add_id>/', account_views.address_update, name='profile-address-update'),
    path('profile/address/delete/<int:add_id>/', account_views.address_delete, name='profile-address-delete')

]
