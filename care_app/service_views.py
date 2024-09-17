from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from care_app.models import ServiceProvider, bookings, Feedback, rating


class IndexView(TemplateView):
    template_name='service_provider/service_home.html'

class IndexViews(TemplateView):
    template_name='service_provider/service_home.html'

class ContacView(TemplateView):
    template_name='service_provider/contact_us.html'

class ViewBooking(TemplateView):
    template_name= 'service_provider/view_bookings.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBooking, self).get_context_data(**kwargs)
        id=ServiceProvider.objects.get(user_id=self.request.user.id)
        user = bookings.objects.filter(serviceprovider_id=id)
        users=ServiceProvider.objects.filter(user__last_name=1)
        context['booking'] = user
        context['users'] = users
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        Id = request.POST['provider']
        serviceid = ServiceProvider.objects.get(id=Id)
        book=bookings.objects.get(id=id)
        book.serviceprovider_id=serviceid.id
        book.save()
        return render(request, 'service_provider/service_home.html',
                      {'message': "redirect service rquest"})

# class approve(TemplateView):
#  def dispatch(self, request, *args, **kwargs):
#         id = self.request.GET['id']
#         cr = bookings.objects.get(id=id)
#         if cr.payment == 'paid':
#            cr.status = 'approved'
#            cr.save()
#            return redirect(request.META['HTTP_REFERER'])
#         else:
#             return render(request, 'service_provider/service_home.html',
#                           {'message': "paid after accept request"})


class approve(TemplateView):
 def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        cr = bookings.objects.get(id=id)
        cr.status = 'approved'
        cr.save()
        return render(request, 'service_provider/service_home.html',
                          {'message': "accepted request"})


class reject(TemplateView):
 def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        booking = bookings.objects.get(id=id)
        booking.status='service rejected'
        booking.save()
        return render(request, 'service_provider/service_home.html',
                          {'message': "request rejected"})


class view_feedback(TemplateView):
    template_name = 'service_provider/view_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(view_feedback, self).get_context_data(**kwargs)
        user_id = ServiceProvider.objects.get(user_id=self.request.user.id)
        feedback = Feedback.objects.filter(serviceprovider_id=user_id.id,status="1")
        context['feedback']= feedback
        return context


class view_rating(TemplateView):
    template_name = 'service_provider/view_rating.html'
    def get_context_data(self, **kwargs):

        context = super(view_rating, self).get_context_data(**kwargs)
        user_id = ServiceProvider.objects.get(user_id=self.request.user.id)
        feedback = rating.objects.filter(serviceprovider_id=user_id.id,status="1")
        context['feedback']= feedback
        return context