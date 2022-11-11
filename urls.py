from django.urls import path 
from.import views



urlpatterns=[
    path('',views.index,name="index"),
    path('registeration/',views.registeration,name="registeration"),
    path('login/',views.login,name="login"),
    path('dash/',views.dash,name="dash"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('dashview/',views.dashview,name="dashview"),
    # path('regworker/',views.regworker,name="regworker"),
]