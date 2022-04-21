from django.urls import path
from . import views


urlpatterns = [
    # method + url 을 통해 어떤 자원을 어떻게 하고 있는지 알 수 있어야함
    # ~/api/v1/articls/
    path('', views.article_list_create),
    path('<int:pk>/', views.article_detail_update_delete),
    path('<int:pk>/comments/', views.article_comment_list_create),
    path('<int:article_pk>/comments/<int:pk>/', views.article_comment_update_delete),

]
