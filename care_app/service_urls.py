from django.urls import path

from care_app.service_views import IndexView, IndexViews, ViewBooking, approve, ContacView, reject, view_feedback, \
    view_rating

urlpatterns=[

    path('',IndexView.as_view()),
    path('servise_home',IndexViews.as_view()),
    path('view_booking',ViewBooking.as_view()),
    path('approve',approve.as_view()),
    path('reject',reject.as_view()),
    path('contact_us',ContacView.as_view()),

    path('view_feedback',view_feedback.as_view()),
    path('view_rating',view_rating.as_view()),


]
def urls():
    return urlpatterns, 'serviceprovider' ,'serviceprovider'