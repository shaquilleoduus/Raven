"""project_raven URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:event_id>/", views.detail, name="detail"),
    path("locations/", views.locations, name="locations"),
    path("locations/<int:location_id>/", views.location_details, name="location_details"),
    # path("date/<int:event_id>/", views.date_details, name="date_details"),
    path("date/<int:event_year>/", views.events_by_year, name="events_by_year"),
    path("date/<int:event_year>/<int:event_month>/", views.events_by_year_month, name="events_by_year_month"),
    path("date/<int:event_year>/<int:event_month>/<int:event_day>/", views.events_by_year_month_day, name="events_by_year_month_day"),
]


