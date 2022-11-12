from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Profile
from .models import UserDetails
# Create your views here.
def index(request):
    # return HttpResponse("this is main page")
    return render(request, 'index.html')
def register(request):
    if request.method=="POST":
        uname =request.POST.get('uname')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        check_profile=Profile.objects.filter(mobile=mobile).first()
        check_user = User.objects.filter(email=email).first()
        if check_profile or check_user :#
            context={'message' : 'User Already Exists ','class':'danger'}
            return render(request,'register.html',context)
        user=User(first_name=uname,email=email)
        user.save()
        #otp=str(random.randint(1000,9999))
        profile=Profile(user=user,mobile=mobile)#,otp=otp
        profile.save()
        #sendotp(mobile,otp)
        request.session['mobile']=mobile
        return redirect('/login')
    return render(request, 'register.html')


def login(request):
    try:
        if request.method == 'POST':
            mobile = request.POST.get('mobile')
            users = Profile.objects.filter(mobile=mobile).first()
            print(users)
            if mobile == users.mobile:
                return redirect('http://127.0.0.1:8000/user')

            else:
                context = {'message': 'User Not Found ', 'class': 'danger'}
                return render(request, 'login.html', context)

        return render(request, 'login.html')
    except TypeError:
        context = {'message': 'User Not Found ', 'class': 'danger'}
        return render(request, 'login.html', context)
    except AttributeError:
        context = {'message': 'User Not Found ', 'class': 'danger'}
        return render(request, 'login.html', context)

def user(request):
    if request.method == 'POST':
        image = request.FILES['image']
        print(image)
        us1 = UserDetails(image=image)
        us1.save()
    return render(request,'user.html')



