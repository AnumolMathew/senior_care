from django.urls import path

from care_app.admin_views import IndexView, New_User, Accepted_User, ApproveView, RejectView, IndexViews, AddCategory, \
    RemoveCategory, NewServiceProviders, ServiceProvidersRejectView, ServiceProvidersApproveView, \
    AcceptedServiceProviders, ViewBooking, view_feedback, view_rating

urlpatterns = [

    path('',IndexView.as_view()),

    path('admin_home',IndexViews.as_view()),
    path('new_user',New_User.as_view()),
    path('accepted_user',Accepted_User.as_view()),
    path('approve', ApproveView.as_view()),
    path('reject', RejectView.as_view()),
    path('add_category',AddCategory.as_view()),
    path('remove_category',RemoveCategory.as_view()),
    path('service_providers',NewServiceProviders.as_view()),
    path('approve_serviceproviders', ServiceProvidersApproveView.as_view()),
    path('reject_serviceproviders', ServiceProvidersRejectView.as_view()),
    path('accepted_service_providers',AcceptedServiceProviders.as_view()),
    path('view_booking',ViewBooking.as_view()),

    path('view_feedback',view_feedback.as_view()),
    path('view_rating',view_rating.as_view()),



    ]
def urls():
    return urlpatterns, 'admin', 'admin'