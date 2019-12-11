from django.urls import path
from .import views

app_name = 'challange'
urlpatterns = [
    path('', views.index, name='index'),
    path('author/', views.author, name='author'),
    path('blog/', views.blog, name='blog'),
    path('mentee/', views.mentee, name='mentee'),
    path('mentor/', views.mentor, name='mentor'),
    path('blog/form', views.blogform, name='blogform'),
    path('submit', views.submit, name='submit' ),
    path('blog/<int:blog_id>', views.seemore, name='seemore')
]