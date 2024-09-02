from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from my.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .models import Events,CustomUser,userstory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def all_events(request):
    all_events = Events.objects.filter(admin=request.user.adminep)
    print("all_events",all_events)
    print()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)
def add_event(request):

    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    #event = Events(staff__created_at_gte=request.user.staff.id)
    #event = Events(staff__id=request.user.staff.id)
    #event = Events(staff=request.user.staff,name=str(title), start=start, end=end)
    event = Events(admin=request.user.adminep,name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)



def singup(request):
    return render(request, 'SingUp.html')
def showloginPage(request):
    return render(request,"login.html")
def home(request):
    return render(request,"home.html")



def hidden(request):
    return render(request, 'error-403.html')
def dologin(request):
    if request.method != "POST":
        return HttpResponseRedirect("error-403")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"),
                                         password=request.POST.get("password"))
        if user is not None:
            login(request, user)
            if user.user_type == "1":
                messages.success(request, "Login successful.")
                return HttpResponseRedirect("login")
            elif user.user_type == "2":
                messages.success(request, "Login successful.")
                return HttpResponseRedirect("login")
            else:
                return HttpResponseRedirect(reverse("login"))
        else:
            messages.error(request, "Invalid credentials. Please try again.")
        return HttpResponseRedirect("login")

def GetUserDetails(request):
    if request.user!=None:
       return HttpResponse ("User :" +request.user.email+"usertype : "+str(request.user.user_type))
    else:
        return HttpResponse("please login frist")


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login')























from django.contrib.auth.models import Group


def signup_user(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")

    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    frist_name = request.POST.get("frist_name")

    try:
        # Create the user
        user = CustomUser.objects.create_user(username=username,first_name=frist_name, password=password, email=email, user_type=1)

        # Get or create the group


        messages.success(request, "Successfully Added Staff")
        return HttpResponseRedirect(reverse("singup"))
    except Exception as e:
        print(e)
        messages.error(request, "Failed to Add Staff")
        return HttpResponseRedirect(reverse("singup"))
