from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.IndexPage,name=""),
    path('register',views.register,name="register"),
    path('my-login',views.my_login,name="my-login"),
    path('HomePage',views.HomePage,name="HomePage"),
    path('UserLogout',views.User_Logout,name="UserLogout"),
    path('profile',views.profile,name="profile"),
    path('Construct',views.Construct,name="Construct"),


]