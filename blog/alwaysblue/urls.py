from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^blog$', views.index, name= 'index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name= 'view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', views.view_category, name='view_blog_category'),
]