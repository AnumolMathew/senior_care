from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from care_app.models import user_reg, UserType, category, ServiceProvider
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

class HomeView(TemplateView):
    template_name = 'home.html'

class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password= request.POST['password']
        user = authenticate(username=email,password=password)

        if user is not None:

            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "service providers":
                    return redirect('/service')
                else:
                    return redirect('/user')

            else:

                return render(request,'home.html',{'message':" User Account Not Authenticated"})
        else:

            return render(request,'home.html',{'message':"Invalid Username or Password"})


class Signup(TemplateView):
    template_name = 'signup.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        phone= request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']

        image = request.FILES['image']
        fi = FileSystemStorage()
        filess = fi.save(image.name, image)

        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects._create_user(username=email,email=email,password=password,first_name=name,is_staff='0',last_name='0')
            user.save()
            users = user_reg()
            users.user_id = user.id
            users.phone=phone
            users.email=email
            users.address = address
            users.Image = filess
            users.username = username
            users.password=password
            users.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            return render(request,'home.html',{'message':"Registration Successfully"})
        except:
            message = "Enter Another Username"
            return render(request, 'signup.html', {'message': message})


class ServiceProviderSignup(TemplateView):
    template_name = 'Service_Provider_SignUp.html'
    def get_context_data(self, **kwargs):
        context = super(ServiceProviderSignup, self).get_context_data(**kwargs)
        Category = category.objects.filter(status='null')
        context['Category'] = Category
        return context

    def post(self , request,*args,**kwargs):
        categ_id = request.POST['categ_id']
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        email = request.POST['email']
        experience = request.POST['experience']
        username = request.POST['username']
        password = request.POST['password']
        image = request.FILES['image']
        fi = FileSystemStorage()
        filess = fi.save(image.name, image)
        IMAGE = request.FILES['document']
        fi = FileSystemStorage()
        filesss = fi.save(IMAGE.name, IMAGE)


        try:
            user = User.objects._create_user(username=email,email=email,password=password,first_name=name,is_staff='0',last_name='0')

            categ = category(id=categ_id)

            Service = ServiceProvider()
            Service.user_id = user.id
            Service.phone=phone
            Service.email=email
            Service.address = address
            Service.username = username
            Service.password=password
            Service.Image  =  filess
            Service.certificate = filesss
            Service.experience = experience
            Service.status = 'null'
            Service.categorys_id = categ.id
            Service.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "service providers"
            usertype.save()
            return render(request,'home.html',{'message':"Registration Successfully"})

        except:
            message = "Enter Another Username"
            return render(request, 'signup.html', {'message': message})


