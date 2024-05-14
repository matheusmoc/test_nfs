from django.urls import path
from. import controller

urlpatterns = [
    path('', controller.Issuance.as_view(), name='index'),
    path('create/', controller.Issuance.as_view(), name='create'),
    path('delete/<int:pk>/', controller.Issuance.as_view(), name='delete'),
    path('update/<int:pk>/', controller.Issuance.as_view(), name='update'),
]