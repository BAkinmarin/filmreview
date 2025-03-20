from django.contrib import admin
from django.urls import path, include, re_path

# Handle images uploaded to Django Administration
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("review.urls"), name="review-urls"),
    re_path
    (r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # path("", include("about.urls"), name="about-urls"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
