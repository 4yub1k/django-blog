"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from users import views as user_views #for different auth and user views, as they have same name (.views)

from app import views as home_views
urlpatterns = [
    path('', home_views.home),#just for test
    path('blog/', include('app.urls')),
    path('register/', user_views.register, name="register"),
    path('update/', user_views.update, name="update"),
    path('blog/<int:post>/', user_views.post, name="post"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    #reset>resetDone>newpassword>newpassworddone. 4 steps
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/reset_pass.html'), name="password_reset"
    ),
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/reset_done.html'), name="password_reset_done"
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/reset_confirm.html'), name="password_reset_confirm"
    ),
        path(
        'password-reset-complete/done/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/reset_complete.html'), name="password_reset_complete"
    ),
    path('admin/', admin.site.urls),

]

""" Make sure you use the correct names for these links, else they will not redirect to them"""
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']