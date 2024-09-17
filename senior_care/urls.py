from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from care_app import admin_urls, user_urls, service_urls
from care_app.views import HomeView, Login, Signup, ServiceProviderSignup
from senior_care import settings

urlpatterns = [

    path('', HomeView.as_view()),
    path('login',Login.as_view()),
    path('service_provider_Signup',ServiceProviderSignup.as_view()),
    path('signup',Signup.as_view()),
    path('admin/', admin_urls.urls()),
    path('user/', user_urls.urls()),
    path('service/',service_urls.urls())


]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
