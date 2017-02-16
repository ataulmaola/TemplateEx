from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'mytemp.views.home', name='home'),
    url(r'^about/$', 'mytemp.views.about', name='about'),
    url(r'^contact/$', 'mytemp.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
] 

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
