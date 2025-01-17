from django.urls import path
from django.contrib.auth import views as auth_views
from pages.views import HomePageView, LoginView, RegisterView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Ana sayfa için URL
    path('login/', LoginView.as_view(), name='login'),  # Login sayfası için URL
    path('register/', RegisterView.as_view(), name='register'),
    
    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt'
    ), name='password_reset'),
    
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),
    
    # Logout URL
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]