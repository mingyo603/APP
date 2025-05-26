from django.urls import path, include
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from .views import BlogSearchView


router = DefaultRouter()
router.register('', BlogViewSet)

urlpatterns =[
    path('blog/', include(router.urls)), 
    path('search/', BlogSearchView.as_view(), name='blog-search'),
]