from django.urls import path
from .views import signup, log_in, log_out


urlpatterns = [
    path('', signup, name='signup'),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('log_out/', log_out, name='logout'),
]
