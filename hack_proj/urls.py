from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('applications.account.urls')),
    path('auth/', include('applications.account.urls')),
    path('category/', include('applications.category.urls')),
    path('product/', include('applications.product.urls')),
    path('order/', include('applications.order.urls')),
    path('review/', include('applications.review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
