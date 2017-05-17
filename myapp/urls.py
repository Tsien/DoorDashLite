from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^customers/$', views.CustomerList.as_view(), name="user-list"),
    url(r'^customers/(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view()),
    url(r'^fooditems/$', views.FoodItemList.as_view(), name="item-list"),
    url(r'^orders/$', views.OrderList.as_view(), name="order-list"),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
    url(r'^orderitem/$', views.OrderItemList.as_view()),
    url(r'^register/$', views.RegistrationView.as_view(), name="register"),
]
'''
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns += [
    url(r'^api-token-auth/', obtain_jwt_token)
]

'''