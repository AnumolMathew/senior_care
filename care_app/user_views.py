from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from care_app.models import ServiceProvider, category, bookings, user_reg, Feedback, rating
from django.contrib.auth.models import User

class IndexView(TemplateView):
    template_name = 'user/user_home.html'


class IndexViews(TemplateView):
    template_name = 'user/user_home.html'


class AboutView(TemplateView):
    template_name = 'user/about_us.html'

class ContactView(TemplateView):
    template_name = 'user/contact_us.html'



class ViewServiceProviders(TemplateView):
    template_name = 'user/view_newserviseproviders.html'
    def get_context_data(self, **kwargs):
        context = super(ViewServiceProviders, self).get_context_data(**kwargs)
        service = ServiceProvider.objects.filter(status='null')
        context['service'] = service
        return context

class SelectCtegory(TemplateView):
    template_name='user/select category.html'
    def get_context_data(self, **kwargs):
        context = super(SelectCtegory, self).get_context_data(**kwargs)
        Category = category.objects.filter(status='null')
        context['Category'] = Category
        return context

    def post(self, request, *args, **kwargs):
        cat = request.POST['categ_id']
        Category = category.objects.get(id=cat)
        service=ServiceProvider.objects.filter(categorys_id=Category.id)
        return render(request, 'user/view_services.html', {'service': service})

class Request(TemplateView):
    template_name= 'user/request.html'
    def get_context_data(self, **kwargs):
        context = super(Request, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        user = ServiceProvider.objects.get(id=id)
        context['id'] = user.id
        return context

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        From_date = request.POST['from_date']
        To_date = request.POST['to_date']
        serviceid = ServiceProvider.objects.get(id=id)

        try:
            Booking =bookings.objects.all()
            for i in Booking:
             # if i.from_date <= From_date and i.to_date <= To_date and i.serviceprovider.id == serviceid.id :

             if i.from_date <= From_date and To_date <= i.to_date and i.serviceprovider.id == serviceid.id:
                print("33333333333")
                return render(request, 'user/user_home.html',
                                      {'message': "slot is already booked, enter another date "})

            else:
                details = request.POST['details']
                service = ServiceProvider.objects.get(id=id)
                booking = bookings()
                booking.from_date = From_date
                booking.to_date = To_date
                booking.status = 'requested'
                booking.payment = 'null'
                booking.details = details
                booking.serviceprovider_id = service.id

                u = User.objects.get(id=self.request.user.id)
                users = user_reg.objects.get(user_id=u.id)
                booking.user_id = users.id
                booking.save()
                return redirect(request.META['HTTP_REFERER'])
        except:
            details = request.POST['details']
            service= ServiceProvider.objects.get(id=id)
            booking = bookings()
            booking.from_date = From_date
            booking.to_date = To_date
            booking.status ='requested'
            booking.payment = 'null'
            booking.details = details
            booking.serviceprovider_id = service.id

            u=User.objects.get(id=self.request.user.id)
            users=user_reg.objects.get(user_id=u.id)
            booking.user_id = users.id
            booking.save()
            return redirect(request.META['HTTP_REFERER'])

class ViewBooking(TemplateView):
    template_name= 'user/view_bookings.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBooking, self).get_context_data(**kwargs)
        id=user_reg.objects.get(user_id=self.request.user.id)
        user = bookings.objects.filter(user_id=id)
        context['booking'] = user
        return context

class Checkout(TemplateView):
    template_name = 'user/checkoutpayment.html'
    def get_context_data(self, **kwargs):

        context = super(Checkout, self).get_context_data(**kwargs)
        id = self.request.GET['id']
        cr = bookings.objects.get(status='approved', id=id)
        context['booking']= cr
        return context

class buynow(TemplateView):
    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        cr = bookings.objects.get(status='approved', id=id)
        if cr.status =='approved':
           cr.payment = 'paid'
           cr.save()
           return render(request,'user/user_home.html',{'message':'Paid Successfully'})
        else:
           return render(request, 'service_provider/service_home.html',
                                  {'message': "paid only accepted the request "})


class feedback(TemplateView):
    template_name = 'user/feedback.html'
    def get_context_data(self, **kwargs):

        context = super(feedback, self).get_context_data(**kwargs)
        service = ServiceProvider.objects.all()
        context['service']= service
        return context

    def post(self, request, *args, **kwargs):
        feedback = request.POST['feedback']
        id = request.POST['id']
        service = ServiceProvider.objects.get(id=id)
        feed = Feedback()
        feed.serviceprovider_id=service.id
        user_id= user_reg.objects.get(user_id=self.request.user.id)
        feed.user_id=user_id.id
        feed.feedback=feedback
        feed.status="1"
        feed.save()
        return render(request, 'user/user_home.html', {'message': 'feedback added successfully'})


class view_feedback(TemplateView):
    template_name = 'user/view_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(view_feedback, self).get_context_data(**kwargs)
        user_id = user_reg.objects.get(user_id=self.request.user.id)
        feedback = Feedback.objects.filter(status="1")
        context['feedback']= feedback
        return context


class ratingg(TemplateView):
    template_name = 'user/ratings.html'
    def get_context_data(self, **kwargs):

        context = super(ratingg, self).get_context_data(**kwargs)
        service = ServiceProvider.objects.all()
        context['service']= service
        return context

    def post(self, request, *args, **kwargs):
        Rat= request.POST['rating']
        id = request.POST['id']
        service = ServiceProvider.objects.get(id=id)
        Ratings = rating()
        Ratings.serviceprovider_id=service.id
        user_id= user_reg.objects.get(user_id=self.request.user.id)
        Ratings.user_id=user_id.id
        Ratings.rating=Rat
        Ratings.status="1"
        Ratings.save()
        return render(request, 'user/user_home.html', {'message': 'rating added successfully'})


class view_rating(TemplateView):
    template_name = 'user/view rating.html'
    def get_context_data(self, **kwargs):

        context = super(view_rating, self).get_context_data(**kwargs)
        user_id = user_reg.objects.get(user_id=self.request.user.id)
        feedback = rating.objects.filter(status="1")
        context['feedback']= feedback
        return context