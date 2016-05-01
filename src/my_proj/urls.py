from django.conf.urls.static import static
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from talks import views
import profiles.urls
import accounts.urls
from gethistoryfile import urls as historyUrls

urlpatterns = [
    # url('r^^home/', views.HomePageView.as_view(), name='my_page'),
    # url(r'^$', views.HomePage.as_view(), name='home'),
    # url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^home/activity', include(historyUrls))
    # url(r'^talks/', include('talks.urls', namespace='talks')),
    # url(r'^history/', include('history.urls', namespace='history')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
