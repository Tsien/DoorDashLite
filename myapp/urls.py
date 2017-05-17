from django.conf.urls import url
from myapp.views import ItemViewSet, api_root, UserViewSet, RegistrationView, OrderViewSet

item_list = ItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

item_detail = ItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

order_list = OrderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

order_detail = OrderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', api_root),

    url(r'^users/$', user_list, name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),

    url(r'^items/$', item_list, name='item-list'),
    url(r'^items/(?P<pk>[0-9]+)$', item_detail, name='item-detail'),

    url(r'^orders/$', order_list, name="order-list"),
    url(r'^orders/(?P<pk>[0-9]+)/$', order_detail, name='order-detail'),

    url(r'^register/$', RegistrationView.as_view(), name="register"),
]

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns += [
    url(r'^api-token-auth/', obtain_jwt_token)
]
