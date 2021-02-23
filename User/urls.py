from django.urls import path

from . import views

urlpatterns = [
    path('',views.user_index,name='user_index'),
    path('<u>',views.user_detail,name="user_detail"),
    path('accounts/login/',views.Login.as_view(),name="login"),
    path('accounts/logout',views.logout_view,name="logout"),
    path('profile/me/',views.me,name="me"),
    path('follow/<int:id>',views.follow,name="follow"),
]
