from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("review.urls"), name="review-urls"),
    path('summernote/', include('django_summernote.urls')),
    # path("", include("about.urls"), name="about-urls"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
