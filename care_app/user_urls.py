from django.urls import path

from care_app.user_views import IndexView, IndexViews, ViewServiceProviders, SelectCtegory, Request, ViewBooking, \
    AboutView, ContactView, Checkout, buynow, feedback, view_feedback, view_rating, ratingg

urlpatterns = [

    path('',IndexView.as_view()),
    path('user_home',IndexViews.as_view()),
    path('view_service_providers',ViewServiceProviders.as_view()),
    path('select_category',SelectCtegory.as_view()),
    path('Request',Request.as_view()),
    path('view_booking',ViewBooking.as_view()),
    path('about_view',AboutView.as_view()),
    path('contact_view',ContactView.as_view()),
    path('Checkout',Checkout.as_view()),
    path('buynow',buynow.as_view()),

    path('feedback',feedback.as_view()),
    path('view_feedback',view_feedback.as_view()),

    path('ratingg', ratingg.as_view()),
    path('view_rating', view_rating.as_view())



    ]
def urls():
    return urlpatterns, 'user', 'user'