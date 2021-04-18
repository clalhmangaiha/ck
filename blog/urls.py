from django.urls import path
from rest_framework_simplejwt import views as jwt_views


from . import views 
urlpatterns = [
    path('',views.index,name='index'),

    path('categories/<int:id>',views.categories,name='category'),

    path('postform/',views.postform,name='postform'),
    path('<int:id>',views.details,name='details'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),

    path('comment/<int:id>',views.comment,name='comment'),
    path('editcomment/<int:id>',views.editcomment,name='editcomment'),
    path('deletecomment/<int:id>',views.deletecomment,name='deletecomment'),

    path('bookmark/<int:id>',views.bookmark,name='bookmark'),

    path('search/',views.search,name='search'),


    path('api/v1',views.PostList.as_view(),name='post_list'),


     path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),


    path('api/v2',views.api_post_index,name='postindex'),
    path('api/v2/<slug>',views.api_post_detail,name='postdetail'),
    path('api/v2/delete/<int:id>',views.api_post_delete,name='postdelete'),
    path('api/v2/edit/<slug>',views.api_post_edit,name='postedit'),
    path('api/v2/create/',views.api_post_create,name='postcreate'),




    

]
