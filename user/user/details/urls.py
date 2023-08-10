from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.table, name="table"),
    path('signup/', views.sign_up, name="signup"),
    path('edit/<int:id>/', views.edit_user, name="edit-user"),
    path('delete/<int:id>/', views.delete_user, name="delete-user"),
    path('login/', views.user_login, name="login-users")

]
