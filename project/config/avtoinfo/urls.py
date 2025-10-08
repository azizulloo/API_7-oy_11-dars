from django.urls import path
from .views import (
    CarApiView, CarDetailApiView,
    BrandCreateView, BrandDetailView,
    ColorCreateView, ColorDetailView,
)

urlpatterns = [
    path("cars/", CarApiView.as_view(), name="car_list"),
    path("cars/<int:car_id>/", CarDetailApiView.as_view()),
    path("brands/", BrandCreateView.as_view()),
    path("brands/<int:pk>/", BrandDetailView.as_view()),
    path("colors/", ColorCreateView.as_view()),
    path("colors/<int:pk>/", ColorDetailView.as_view()),
]
