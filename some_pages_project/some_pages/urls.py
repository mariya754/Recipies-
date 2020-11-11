from django.urls import path
from . import views

urlpatterns = [
    path('', views.RecepiesPageView.as_view(), name='recepies'),
    path('vanilla.html/', views.VanillaCakePageView.as_view(), name='vanilla'),
    path('chocolate.html/', views.ChocolateCakePageView.as_view(), name='chocolate'),
    path('red-velvet.html/', views.RedVelvetCakePageView.as_view(), name='red-velvet'),
    path('cream.html/', views.CreamCheesePageView.as_view(), name='cream'),
]