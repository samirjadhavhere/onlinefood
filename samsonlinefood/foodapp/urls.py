from django.urls import path
from . import views as v

urlpatterns=[
    path("",v.home),
    path("-register",v.reguser,name="reg"),
    path("-Login",v.userlogin,name="log"),
    #ath("-Logout",v.userlogout,name="logout"),
    #path("-Edit",v.edituser,name="edt")
    
]
