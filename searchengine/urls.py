from django.views.generic import TemplateView
from django.urls import path,include
from .views import SignUpView, profile
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/',profile, name='profile'),
    # path('search/password_reset/', changePassword, name="password_reset")
    # path('base/', TemplateView.as_view(template_name='base.html'), name='base'),
    # path('login/', TemplateView.as_view(template_name='registration/login.html'), name='login'),
    # path('search/home/', TemplateView.as_view(template_name='home.html'), name='home'),
	path('password_change/',
     auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"),
     name="password_change"),
	path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
     auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_sent.html"), 
     name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_done.html"), 
        name="password_reset_complete"),
]