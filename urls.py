from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView,name="home"),
    path('details/',views.detailsView,name="details"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('payment/',views.paymentView,name="payment"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(),name="logout"),
]