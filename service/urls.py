from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict', views.predict, name='predict'),
    path('result', views.result, name='result'),
    path('cut', views.cut, name='cut'),
    path('denoising', views.denoising, name='denoising'),

    path('predict2', views.predict2, name='predict2'),
]
