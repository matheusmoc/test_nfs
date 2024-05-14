from django.urls import path
from. import controller

urlpatterns = [
    path('', controller.IssuanceViewIndex.as_view(), name='index'),
    path('create/', controller.IssuanceViewIndexCreate.as_view(), name='create'),
    path('delete/<int:pk>/', controller.IssuanceViewIndexDelete.as_view(), name='delete'),
    path('update/<int:pk>/', controller.IssuanceViewIndexUpdate.as_view(), name='update'),
]