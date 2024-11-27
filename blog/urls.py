from django.urls import path

from .views import views

urlpatterns = [
    path('', post_view.PostView.as_view(), name='home'),
]
