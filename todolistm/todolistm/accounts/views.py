from django.shortcuts import render, redirect


# Create your views here.
def account_settings_account(request):
    return render(request, 'account.html')


def account_settings_notifications(request):
    return render(request, 'notifications.html')


def account_settings_connections(request):
    return render(request, 'connections.html')


def authentications_login(request):
    return render(request, 'account-login.html')


def authentication_register(request):
    return render(request, 'account-register.html')


def forgot_password(request):
    return render(request, 'account-forgot-password.html')


def misc_error(request):
    return render(request, 'misc-error.html')


def misc_under_maintenance(request):
    return render(request, 'misc-under-maintenance.html')