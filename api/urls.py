from django.conf.urls import url
from . import views

urlpatterns = [
	# url(r'^$', views.Index.as_view(), name='index'),
	url(r'^user/all/$', views.UserBaseInformations.as_view(), name='user-all'),
	url(r'^user/washman/$', views.WashMan.as_view(), name='user-all'),
	url(r'^user/login/$', views.UserLogin.as_view(), name='user-login'),
	url(r'^user/signup/$', views.UserSignUp.as_view(), name='user-login'),
	url(r'^email/exist/$', views.EmailExist.as_view(), name='email-exist'),

	# order
	url(r'^order/new/$', views.OrderNew.as_view(), name='order-new'),
	url(r'^order/taking/$', views.OrderTaking.as_view(), name='order-taking'),
	url(r'^order/washing/$', views.OrderWashing.as_view(), name='order-washing'),
	url(r'^order/washed/$', views.OrderWashed.as_view(), name='order-washed'),
	url(r'^order/returning/$', views.OrderReturning.as_view(), name='order-returning'),
	url(r'^order/arrived/$', views.OrderArrived.as_view(), name='order-arrived'),
	url(r'^order/all/arrived/$', views.OrderAllArrived.as_view(), name='order-arrived'),
	url(r'^order/me/taking/$', views.TakingPending.as_view()),
	url(r'^order/all/taking/$', views.AllTakingPending.as_view()),
	url(r'^order/me/returning/$', views.ReturningPending.as_view(), name='order-taking'),
	url(r'^order/me/washing/$', views.WashingPending.as_view(), name='order-taking'),
	url(r'^order/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='order-taking'),
	url(r'^order/list/$', views.OrderList.as_view(), name='order-taking'),

	# catagory
	url(r'^category/$', views.CategoryAPI.as_view(),name='catagories'),

	# product
	url(r'^product/$', views.ProductAPI.as_view(), name='product'),

	url(r'^user/(?P<pk>[0-9]+)/$',views.UserDetailInformations.as_view(), name='user-detail'),
	url(r'^user/me/$',views.UserMeInformations.as_view(), name='user-detail'),
	url(r'^address/city/$',views.Cities.as_view(), name='user-detail'),
	url(r'^address/city/(?P<pk>[0-9]+)/$',views.Districts.as_view(), name='user-detail'),
]
