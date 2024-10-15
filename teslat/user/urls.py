from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/edit_profile/', views.UserEditProfileView.as_view(), name='edit_profile'),
    path('profile/change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('profile/order_history/', views.OrderHistoryView.as_view(), name='order_history'),
]