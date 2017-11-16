from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.Index.as_view(), name='index'),
	url(r'^user/all/$', views.UserBaseInformations.as_view(), name='user-all'),
	url(r'^user/login/$', views.UserLogin.as_view(), name='user-login'),
	url(r'^user/signup/$', views.UserSignUp.as_view(), name='user-login'),
	url(r'^email/exist/$', views.EmailExist.as_view(), name='email-exist'),
	url(r'^order/new/$', views.OrderNew.as_view(), name='order-new'),
	url(r'^order/taking/$', views.OrderTaking.as_view(), name='order-taking'),
	url(r'^order/returning/$', views.OrderReturning.as_view(), name='order-taking'),
	url(r'^order/arrived/$', views.OrderArrived.as_view(), name='order-arrived'),
	url(r'^order/me/taking/$', views.TakingPending.as_view(), name='order-taking'),
	url(r'^order/me/returning/$', views.ReturningPending.as_view(), name='order-taking'),
	url(r'^user/(?P<pk>[0-9]+)/$',views.UserDetailInformations.as_view(), name='user-detail'),
	url(r'^address/city/$',views.Cities.as_view(), name='user-detail'),
	url(r'^address/city/(?P<pk>[0-9]+)/$',views.Districts.as_view(), name='user-detail'),
]
