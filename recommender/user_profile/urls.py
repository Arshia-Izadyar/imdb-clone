from django.urls import path
from .views import CustomLogout, ProfileView

app_name = "profile"



urlpatterns = [
    path('logout/', CustomLogout.as_view(), name="logout"),
    path('', ProfileView.as_view(), name="profile")
]
