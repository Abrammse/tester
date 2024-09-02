from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from my.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .models import Events,CustomUser, userstory,AdminHOD,Staffs,testcases
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#cont = userstory.objects.filter(staff__id=request.user.staff.id).count()
def tester(request):
    cont=userstory.objects.filter(staff__id=request.user.staff.id).count()
    conts=testcases.objects.filter(staff_id=request.user.staff.id).count()

    user_info = {
        'username': request.user.username,
    }

    context = {
        #"events": all_events,
        'user_info': user_info,
        'cont':cont,
        'conts':conts

    }

    return render(request, 'tester.html', context)


from django.http import JsonResponse
from .models import Events

def all_event(request):
    all_events = Events.objects.filter(admin__id=request.user.staff.admin.adminep.id)
    print(all_events)
    out = []
    for event in all_events:
        start_date = event.start.strftime("%m/%d/%Y, %H:%M:%S") if event.start else None
        end_date = event.end.strftime("%m/%d/%Y, %H:%M:%S") if event.end else None
        out.append({
            'title': event.name,
            'id': event.id,
            'start': start_date,
            'end': end_date,
        })

    return JsonResponse(out, safe=False)


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(staff=request.user.staff,name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update_event(request):
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

def testerview(request):
       Ayadata = userstory.objects.filter(staff__id=request.user.staff.id)
       user_info = {
           'username': request.user.username,
       }

       data = {
          'Ayadata': Ayadata,
           'user_info':user_info

        }
       print(Ayadata)

       return render(request, "view user  tester .html", data)


def y_testcases(request):
    Ayadata = userstory.objects.filter(staff__id=request.user.staff.id)
    userdata = Staffs.objects.filter(id=request.user.id)
    user_info = {
        'username': request.user.username,
    }

    data = {
        'Ayadata': Ayadata,
        'userdata':userdata,
        'user_info':user_info
    }
    return render(request, "enter test case .html" ,data)

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import testcases, userstory

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import testcases, userstory

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import testcases, userstory, Staffs

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib import messages
from .models import testcases, userstory, Staffs

def add_testcase(request):
    if request.method != "POST":
        return HttpResponseRedirect("error-403")

    select_userstory_id = request.POST.get("select_userstory")
    title = request.POST.get("title")
    description = request.POST.get("description")

    try:
        userstory_instance = userstory.objects.get(id=select_userstory_id)
        kvkd = Staffs.objects.get(id=request.user.staff.id)

        # Create a new test case with the provided details
        testcase = testcases.objects.create(
            title=title,
            userstory_d=userstory_instance,
            bady=description,
            staff_id=kvkd
        )

        messages.success(request, "Successfully Added User Story")
        return HttpResponseRedirect(reverse("y_testcases"))
    except userstory.DoesNotExist:
        messages.error(request, "User story not found. Please select a valid user story.")
        return HttpResponseRedirect(reverse("y_testcases"))
    except Staffs.DoesNotExist:
        messages.error(request, "Staff not found. Please ensure you are logged in as a valid staff member.")
        return HttpResponseRedirect(reverse("y_testcases"))
    except Exception as e:
        print(e)  # Log the exception for debugging
        messages.error(request, "Failed to Add User Story")
        return HttpResponseRedirect(reverse("y_testcases"))

def viwer_testcases(request):
    Ayadata = testcases.objects.filter(staff_id=request.user.staff.id)
    user_info = {
        'username': request.user.username,
    }

    data = {
        'Ayadata': Ayadata,
        'user_info':user_info
    }
    return render(request, "view user  tester3 .html" ,data)
