from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('pricing/',views.Pricing,name='pricing'),
    path('contact/',views.Contact,name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)