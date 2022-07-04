"""app URL Configuration

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
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve
from signup import views as signup_views



# Adds site header, site title, index title to the admin side.
admin.site.site_header = "Company Name"
admin.site.site_title = "Company Title"
admin.site.index_title = "Index Title"


urlpatterns = [
    url(r"^signup/$", signup_views.signup, name="signup"),  # Allows users to Signup through webapp.
    path("admin/", admin.site.urls),  # Allows admin page views.
    path("accounts/", include("django.contrib.auth.urls")),  # Allows user auth through webapp backend.
    url(r"^oauth/", include("social_django.urls", namespace="social")),
    path("", include("home.urls")),  # Landing page urls.
    path("", include("contact.urls")),  # Contact us form urls.
    path("", include("process.urls")),  # Process order form.
    path("", include("verify.urls")),  # Verify product form.
    path("", include("pack.urls")),  # pack order form.
    path("", include("todo.urls")),  # task_todo form.
    path("", include("inventory.urls", namespace="api")),  # In browser inventoy API view.
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(
        r"^site/(?P<path>.*)$",
        serve,
        {"document_root": os.path.join(BASE_DIR, "site"), "show_indexes": True},
        name="site_path",
    ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path(
        "favicon.ico",
        serve,
        {
            "path": "favicon.ico",
            "document_root": os.path.join(BASE_DIR, "home/static"),
        },
    ),
]


# Switch to social login if it is configured - Keep for later
try:

    social_login = "registration/login_social.html"
    urlpatterns.insert(
        0,
        path(
            "accounts/login/", auth_views.LoginView.as_view(template_name=social_login)
        ),
    )
    print("Using", social_login, "as the login template")
except:
    print("Using registration/login.html as the login template")


# References

# https://docs.djangoproject.com/en/3.0/ref/urls/#include

