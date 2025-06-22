from django.urls import path
from .views import register_view, login_view, profile_view, logout_view, safe_input_view, upload_file_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('safe-input/', safe_input_view, name='safe-input'),
]
