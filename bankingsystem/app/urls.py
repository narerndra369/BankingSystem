from django.urls import path
from app import views
urlpatterns=[
    path('login',views.loginview,name="login"),
    path('logout1', views.logout1, name='logout'),
    path('home',views.home,name="home"),
    path('register',views.register,name="register"),
    path('balance',views.balance,name="balance"),
    path('transfer',views.transfer,name="transfer"),
    path('transactionhistory',views.transactionhistory,name="transactionhistory")
]
