from django.urls import path

from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("register",views.register_view,name="register"),
    path("logout",views.logout_view,name="logout"),
    path("Data_Sheet/<int:id>",views.data_sheet,name="Data_Sheet"),
    path("Data_Sheet/Rate_Dr/<int:id>",views.Rate_Dr,name="Rate_Dr"),
]