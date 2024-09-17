from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import render, redirect

from care_app.models import user_reg, category, ServiceProvider, bookings, Feedback, rating


class IndexView(TemplateView):
    template_name = 'admin/admin_home.html'


class IndexViews(TemplateView):
    template_name = 'admin/admin_home.html'

class New_User(TemplateView):
    template_name = 'admin/new users.html'
    def get_context_data(self, **kwargs):
        context = super(New_User,self).get_context_data(**kwargs)
        new_user = user_reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
        context['newuser'] = new_user
        return context

class Accepted_User(TemplateView):
    template_name = 'admin/accepted users.html'
    def get_context_data(self, **kwargs):
        context = super(Accepted_User,self).get_context_data(**kwargs)
        accepteduser = user_reg.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        context['accepteduser'] = accepteduser
        return context

class ApproveView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=User.objects.get(id=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_home.html',{'message':" Account Approved"})

class RejectView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=User.objects.get(id=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_home.html',{'message':"Account Removed"})


class AddCategory(TemplateView):
    template_name = 'admin/add_category.html'

    def get_context_data(self, **kwargs):
        context = super(AddCategory, self).get_context_data(**kwargs)
        Category = category.objects.filter(status='null')
        context['Category'] = Category
        return context

    def post(self , request,*args,**kwargs):
        categorys = request.POST['category']
        details = request.POST['details']
        price = request.POST['price']
        Category = category()
        Category.category = categorys
        Category.details = details
        Category.price = price
        Category.status = 'null'
        Category.save()
        return redirect(request.META['HTTP_REFERER'])

class RemoveCategory(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        Categ=category.objects.get(id=id)
        Categ.status='remove'
        Categ.save()
        return redirect(request.META['HTTP_REFERER'])


class NewServiceProviders(TemplateView):
    template_name = 'admin/view_newserviseproviders.html'
    def get_context_data(self, **kwargs):
        context = super(NewServiceProviders, self).get_context_data(**kwargs)
        service = ServiceProvider.objects.filter(status='null')
        context['service'] = service
        return context


class AcceptedServiceProviders(TemplateView):
    template_name = 'admin/accepted_serviceproviders.html'
    def get_context_data(self, **kwargs):
        context = super(AcceptedServiceProviders, self).get_context_data(**kwargs)
        service = ServiceProvider.objects.filter(status='approved')
        context['service'] = service
        return context



class ServiceProvidersApproveView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=ServiceProvider.objects.get(id=id)
        users = User.objects.get(id=user.user.id)
        user.status='approved'
        users.last_name = '1'
        user.save()
        users.save()
        return redirect(request.META['HTTP_REFERER'])

class ServiceProvidersRejectView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id=request.GET['id']
        user=ServiceProvider.objects.get(id=id)
        users = User.objects.get(id=user.user.id)
        user.status='remove'
        users.last_name = '1'
        users.is_active = '0'
        user.save()
        users.save()
        return redirect(request.META['HTTP_REFERER'])

class ViewBooking(TemplateView):
    template_name= 'admin/view_bookings.html'
    def get_context_data(self, **kwargs):
        context = super(ViewBooking, self).get_context_data(**kwargs)
        user = bookings.objects.all()
        context['booking'] = user
        return context


class view_feedback(TemplateView):
    template_name = 'admin/view_feedback.html'
    def get_context_data(self, **kwargs):

        context = super(view_feedback, self).get_context_data(**kwargs)
        feedback = Feedback.objects.filter(status="1")
        context['feedback']= feedback
        return context

class view_rating(TemplateView):
    template_name = 'admin/view_rating.html'
    def get_context_data(self, **kwargs):

        context = super(view_rating, self).get_context_data(**kwargs)
        feedback = rating.objects.filter(status="1")
        context['feedback']= feedback
        return context