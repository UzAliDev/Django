from django.urls import path
from .views import SingUpView

urlpatterns = [
    path('signup/', SingUpView.as_view(), name = 'signup'),
]