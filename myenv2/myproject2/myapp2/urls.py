"""
URL configuration for myproject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("productDetails/", views.productDetails, name="productDetails"),
    path("orderComplete/", views.orderComplete, name="orderComplete"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("cpass/", views.cpass, name="cpass"),
    path("fpass/", views.fpass, name="fpass"),
    path("newpass/", views.newpass, name="newpass"),
    path("otp/", views.otp, name="otp"),
    path("scpass/", views.scpass, name="scpass"),
    path("profile/", views.profile, name="profile"),
    path("sindex/", views.sindex, name="sindex"),
    path("men/", views.men, name="men"),
    path("add/", views.add, name="add"),
    path("viewProduct/", views.viewProduct, name="viewProduct"),
    path("updateProduct/<int:pk>/", views.updateProduct, name="updateProduct"),
    path("deleteProd/<int:pk>/", views.deleteProd, name="deleteProd"),
    path("cart/", views.cart, name="cart"),
    path("addcart/<int:pk>/", views.addcart, name="addcart"),
    path("deletecart/<int:pk>/", views.deletecart, name="deletecart"),
    path("changeqty/<int:pk>/", views.changeqty, name="changeqty"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("addwish/<int:pk>/", views.addwish, name="addwish"),
    path("deletewish/<int:pk>/", views.deletewish, name="deletewish"),
    path("applycoupon/", views.applycoupon, name="applycoupon"),
    path("cancelcoupon/", views.cancelcoupon, name="cancelcoupon"),
    path("checkout/<int:pk>/", views.checkout, name="checkout"),
    path("success/", views.success, name="success"),
    path("error/", views.error, name="error"),
    path("create_order/<int:pk>/", views.create_order, name="create_order"),
]
