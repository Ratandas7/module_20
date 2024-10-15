from django.urls import path
from . import views

urlpatterns = [
    path('<slug:model_slug>/<int:pk>/', views.CarDetailView.as_view(), name='car_details'),
    path('order_now/<slug:model_slug>/<int:id>/', views.order_now, name='order_now'),
]