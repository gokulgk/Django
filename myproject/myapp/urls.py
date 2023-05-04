from django.urls import path
from . import views


urlpatterns = [
    path('A/', views.my_view, name='my_view'),
    path('B/', views.my_view2, name='my_view2'),
    path('C/', views.my_view3, name='my_view3'),
    path('D/', views.my_view4, name='my_view4'),
    path('csv/', views.csv_view, name='csv_view'),
    path('login/', views.login, name='login'),
]
