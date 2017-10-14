from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.Index.as_view(), name='index'),
	url(r'^user/all/$', views.UserBaseInformations.as_view(), name='user-all'),
	url(r'^user/login/$', views.UserLogin.as_view(), name='user-login'),
	url(r'^user/(?P<pk>[0-9]+)/$',views.UserDetailInformations.as_view(), name='user-detail'),
]
