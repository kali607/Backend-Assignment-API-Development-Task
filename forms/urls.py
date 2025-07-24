from django.urls import path
from . import views

urlpatterns = [
    path('bogie/', views.BogieChecksheetFormAPIView.as_view(), name='bogie-form'),
    path('wheel/', views.WheelSpecificationFormAPIView.as_view(), name='wheel-form'),

    path('bogie/list/', views.BogieFormListView.as_view(), name='bogie-form-list'),
    path('wheel/list/', views.WheelFormListView.as_view(), name='wheel-form-list'),
]
