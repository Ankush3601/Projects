from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.index, name="index"),
    path('add/', views.add_task, name='add_task'),
    path('', views.login_form, name="login"),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('without_menu/', views.layouts_without_menu, name="layouts-without-menu"),
    path('layouts-without-navbar', views.layouts_without_navbar, name="layouts-without-navbar"),
    path('layouts-container/', views.layouts_container, name="layouts-container"),
    path('layouts-fluid/', views.layouts_fluid, name="layouts-fluid"),
    path('layouts-blank/', views.layouts_blank, name="layouts-blank"),
]
