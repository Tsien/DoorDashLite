from django.conf.urls import url
from myapp.views import ItemViewSet, api_root, UserViewSet, RegistrationView, OrderViewSet, OrderItemViewSet
from myapp import views

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

oi_list = OrderItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

oi_detail = OrderItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', api_root),

    url(r'^users/$', user_list, name="user-list"),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),

    url(r'^items/$', views.ItemList.as_view(), name='item-list'),
    url(r'^items/(?P<pk>[0-9]+)$', item_detail, name='item-detail'),

    url(r'^orderitems/$', oi_list, name='oi-list'),
    url(r'^orderitems/(?P<pk>[0-9]+)$', oi_detail, name='oi-detail'),

    url(r'^orders/$', order_list, name="order-list"),
    url(r'^orders/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view(), name='order-detail'),
    url(r'^orders/(?P<pk>[0-9]+)/items$', views.AddItemView.as_view(), name='add-item'),

    url(r'^register/$', RegistrationView.as_view(), name="register"),
]

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns += [
    url(r'^api-token-auth/', obtain_jwt_token)
]
