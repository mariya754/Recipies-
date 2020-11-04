from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecepiesPageView.as_view(), name='recepies'),
    path('vanilla/', views.VanillaCakePageView.as_view(), name='vanilla'),
    path('chocolate/', views.ChocolateCakePageView.as_view(), name='chocolate'),
    path('red-velvet/', views.RedVelvetCakePageView.as_view(), name='red-velvet'),
    path('cream/', views.CreamCheesePageView.as_view(), name='cream'),
]