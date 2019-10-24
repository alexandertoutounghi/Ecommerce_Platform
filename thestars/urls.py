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
from goods.views import GoodsListViewSet, CategoryViewset
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from user_operation.views import UserFavViewset
from users.views import UserViewset

router = DefaultRouter()

# configure goods url
router.register(r'goods', GoodsListViewSet, base_name="goods")
# configure category url
router.register(r'categorys', CategoryViewset, base_name="categorys")
# configure users url
router.register(r'users', UserViewset, base_name="users")
# Wish list
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

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
