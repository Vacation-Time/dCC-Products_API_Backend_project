from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('image_upload', image_view, name='image_upload'),
    path('success', success, name='success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('', views.products_list),
    path('product_images', display_images, name='product_images'),
    path('<int:pk>/', views.products_detail)
]
