from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView



from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("signup/", views.signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    
]