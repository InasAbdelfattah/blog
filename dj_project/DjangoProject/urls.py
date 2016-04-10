from django.conf.urls import patterns , include , url
from django.contrib import admin
from DjangoApp import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import password_reset
from DjangoApp.views import Article_create , Article_Edit , register
from django.conf.urls.static import static

admin.autodiscover()




urlpatterns = [
	url(r'^admin/',admin.site.urls),
	url(r'^home/$',views.home),
	url(r'^login/$',views.auth_views.login,name="login"),
	url(r'^logout/$',views.auth_views.logout,name="logout"),
	url(r'^$',views.index),
	url(r'^Article/create/$',Article_create),
	url(r'^(?P<article_id>[0-9]+)/edit/$',Article_Edit),
	url(r'^register/$', register),
	url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : '/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
	url(r'^user/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : '/user/password/done/'}),
    url(r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
	# url(r'^comments/', include('django_comments.urls')),

	url(r'^edit/', views.edit_view),
	url(r'^index/(?P<article_id>[0-9]+)/details/$',views.details),
	url(r'^index/(?P<article_id>[0-9]+)/add/$',views.add),
	#url(r'^index/(?P<article_id>[0-9]+)/add/$',views.reply),
	url(r'^reply/(?P<article_id>[0-9]+)/(?P<comment_id>[0-9]+)/$',views.reply),
	url(r'^index/GetAllArticle/$',views.GetAllArticle),
	url(r'^delete/(?P<comment_id>[0-9]+)/$',views.Delete_comment),
	url(r'^mark/(?P<article_id>[0-9]+)/$',views.mark),
	url(r'^accounts/', include('allauth.urls')),
    url(r'^mark/(?P<article_id>[0-9]+)/$',views.marked),
	url(r'^unmark/(?P<article_id>[0-9]+)/$',views.unmarked),
	url(r'^like/(?P<comment_id>[0-9]+)/$',views.liked),
	url(r'^unlike/(?P<comment_id>[0-9]+)/$',views.unliked),
   


    # url(r'^delete/post/(?P<p_id>[0-9]+)/$',removepost),

	# #url(r'^profile/$',views.profile,name="profile"),
	

]

# if settings.DEBUG:
# 	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)