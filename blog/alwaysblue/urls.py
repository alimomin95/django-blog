from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^blog$', views.index, name= 'index'),
    url(r'^login$', views.view_login, name='login'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name= 'view_blog_post'),
    url(r'^blog/tag/(?P<slug>[^\.]+).html', views.view_tag, name='view_blog_tag'),
    url(r'^blog/author/(?P<slug>[^\.]+).html', views.view_author, name='view_blog_author'),
]
