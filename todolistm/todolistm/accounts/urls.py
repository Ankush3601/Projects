from . import views
from django.urls import path

urlpatterns = [
    path('account/', views.account_settings_account, name="account-settings-account"),
    path('notifications/', views.account_settings_notifications, name="account-settings-notifications"),
    path('connections/', views.account_settings_connections, name="account-settings-connections"),
    path('login/', views.authentications_login, name="account-login"),
    path('register/', views.authentication_register, name="account-register"),
    path('forgot-password/', views.forgot_password, name="forgot-password"),
    path('error/', views.misc_error, name="misc-error"),
    path('under_maintenance/', views.misc_under_maintenance, name="under-maintenance")
]
