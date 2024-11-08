from django.urls import path
from. import controller

urlpatterns = [
    path('', controller.IssuanceIndexView.as_view(), name='index'),
    path('create/', controller.IssuanceCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', controller.IssuanceDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', controller.IssuanceEditView.as_view(), name='edit'),
]