from django.urls import path

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

    

]
