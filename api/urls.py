from django.contrib import admin
from django.urls import path
from django.urls import path, include        # add this
from django.conf import settings             # add this
from django.conf.urls.static import static   # add this

urlpatterns = [
    path('', admin.site.urls),
    path("detective/", include('core.urls')),
    path("core/", include('core.urls')),
    path("sovet/", include('sovet.urls')),
    path('admin_tools/', include('admin_tools.urls'))
]

# add this
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
