from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),
    # path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.register, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout")
]

urlpatterns += [
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name="password_reset.html",
        email_template_name='password_reset_email.html'
    ), name="password_reset"),

    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"
    ), name="password_reset_done"),

    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"
    ), name="password_reset_confirm"),

    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"
    ), name="password_reset_complete"),
]