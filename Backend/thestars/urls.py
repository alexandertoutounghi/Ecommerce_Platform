"""thestars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from thestars.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet, CategoryViewset, HotSearchsViewset, BannerViewset, IndexCategoryViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from trade.views import ShoppingCartViewset, OrderViewset
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from users.views import UserViewset, SmsCodeViewset

router = DefaultRouter()

# configure goods url
router.register(r'goods', GoodsListViewSet, base_name="goods")
# configure category url
router.register(r'categorys', CategoryViewset, base_name="categorys")
# configure users url
router.register(r'users', UserViewset, base_name="users")
# Wish list
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
# # Popular search
# router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")
# Comments
router.register(r'messages', LeavingMessageViewset, base_name="messages")
# Shipping address
router.register(r'address', AddressViewset, base_name="address")
# Shopping cart URL
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
# Order relevant URL
router.register(r'orders', OrderViewset, base_name="orders")
# Banners relevant URL on HomePage (Featured Products)
router.register(r'banners', BannerViewset, base_name="banners")
# Product Series Data
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

# Registration Code
router.register(r'codes', SmsCodeViewset, base_name="codes")


urlpatterns = [
    url('xadmin/', xadmin.site.urls),
    url('media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    url(r'^', include(router.urls)),
    # Documentation (Remove $ sign!)
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title="TheStars")),
    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),

]
