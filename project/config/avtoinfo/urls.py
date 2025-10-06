from django.urls import path
from .views import CartApiView, CarDetailApiView

urlpatterns = [
    path("cars/", CartApiView.as_view()),
    path("cars/create/", CartApiView.as_view()),
    path("cars/<int:car_id>/", CarDetailApiView.as_view()),
    # path("cars/<int:pk>/", CarApiView.as_view()),
]