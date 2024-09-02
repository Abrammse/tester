from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from my.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from .models import Events,CustomUser,userstory,AdminHOD,Staffs,testcases
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db.models import Q
def index(request):
    admin = CustomUser.objects.get(id=request.user.id)
    admin_hod = AdminHOD.objects.get(admin=admin)
    cont = userstory.objects.filter(admin=admin_hod).count()
    staffs = Staffs.objects.filter(admin=admin).count()
    conts = testcases.objects.filter(userstory_d__admin=admin_hod).count()



    user_info = {
        'username': request.user.username,
    }

    context = {
        "events": all_events,
        'cont': cont,
        'staffs': staffs,
        'user_info': user_info,
        'conts':conts,

    }

    return render(request, 'index.html', context)
def viewtest_case(request):
    admin = CustomUser.objects.get(id=request.user.id)
    admin_hod = AdminHOD.objects.get(admin=admin)
    test_case = testcases.objects.filter(userstory_d__admin=admin_hod)
    user_info = {
        'username': request.user.username,
    }
    context={
        "test_case":test_case,
        "user_info":user_info
    }
    return render(request, "view user  tester4 .html",context)

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Events



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


def user_story(request):
    admin = CustomUser.objects.get(id=request.user.id)
    users=Staffs.objects.filter(admin=admin)

    user_info = {
        'username': request.user.username,
    }
    context={
        "users":users,
        "user_info":user_info
    }
    return render(request, "enter user story .html",context)
def viewtesters(request):
    admin = CustomUser.objects.get(id=request.user.id)
    print(admin)
    admin_hod = AdminHOD.objects.get(admin=admin)
    print(admin_hod)
    staffs = userstory.objects.filter(admin=admin_hod)
    print(staffs)
    user_info = {
        'username': request.user.username,
    }
    # Pass the user story to the template

    return render(request, "view user story .html", {'staffs': staffs,'user_info':user_info,
})
def viewteste(request):
    admin=CustomUser.objects.get(id=request.user.id)
    staffs = Staffs.objects.filter(admin=admin)
    user_info = {
        'username': request.user.username,
    }
    return render(request, "view user story  - Copy.html", {"staffs": staffs,"user_info":user_info} )
def delete_staff_instance(request, pk):
    try:
        staff = get_object_or_404(Staffs, id=pk)

        staff.delete()

        messages.success(request, "Successfully Deleted Staff")
    except CustomUser.DoesNotExist:
        messages.error(request, "Admin user not found.")
    except Staffs.DoesNotExist:
        messages.error(request, "Staff not found.")
    except Exception as e :
        messages.error(request, "you must user story related by tester")


    return redirect('view-tester')
def delete_story(request, pk):
    story = get_object_or_404(userstory, id=pk)
    story.delete()
    messages.success(request, "Successfully Deleted User Story")
    return redirect('view-user stories')
def edit_staff(request,staff_id):
    admin = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(id=staff_id)
    user_info = {
        'username': request.user.username,
    }
    return render(request, "enter tester - Copy.html", {"staff": staff, "id": staff_id,"user_info":user_info})
def edit_user(request,staff_id):
    admin = CustomUser.objects.get(id=request.user.id)
    staff = userstory.objects.get(id=staff_id)
    user_info = {
        'username': request.user.username,
    }
    return render(request, "edit user story .html", {"staff": staff, "id": staff_id,"user_info":user_info})




def add_user(request):
    if request.method != "POST":
        return HttpResponseRedirect("error-403")

    title = request.POST.get("title")
    description = request.POST.get("description")
    select_user_id = request.POST.get("select_user")

    if not title or not description or not select_user_id:
        messages.error(request, "Please fill in all required fields.")
        return HttpResponseRedirect(reverse("add user story"))

    try:
        # Assuming CustomUser has a OneToOneField relationship with Staffs
        adminuser = CustomUser.objects.get(id=request.user.id)
        admin_hod = AdminHOD.objects.get(admin=adminuser)
        # Retrieve the selected staff based on the user ID from the form
        selected_staff = Staffs.objects.get(id=select_user_id)

        new_user_story = userstory.objects.create(title=title, description=description, staff=selected_staff,admin=admin_hod,
                                                  active=True)
        messages.success(request, "Successfully Added User Story")
        return HttpResponseRedirect(reverse("add"))
    except Staffs.DoesNotExist:
        messages.error(request, "Staff not found. Please select a valid staff.")
        return HttpResponseRedirect(reverse("add user story"))
    except CustomUser.DoesNotExist:
        messages.error(request, "Admin user not found.")
        return HttpResponseRedirect(reverse("add user story"))
    except Exception as e:
        print(e)  # Log the exception for debugging
        messages.error(request, "Failed to Add User Story")
        return HttpResponseRedirect(reverse("add"))
def addtester(request):
    staffs = Staffs.objects.all()
    adminuser = CustomUser.objects.get(id=request.user.id)
    user_info = {
        'username': request.user.username,
    }
    print(adminuser)
    return render(request, "enter tester.html", {"staffs": staffs,"user_info":user_info})

from django.core.exceptions import ObjectDoesNotExist
def add_staff_save(request):
    if request.method != "POST":
        return HttpResponseRedirect("error-403")

    first_name = request.POST.get("first_name")
    email = request.POST.get("email")
    password = request.POST.get("password")
    username = request.POST.get("username")
    #print(request.user.id)

    try:
        # Create a new CustomUser with the provided details
        adminuser= CustomUser.objects.get(id=request.user.id)
        #adminprofile=AdminHOD.objects.get(admin=adminuser)
        try:
            user = CustomUser.objects.create_user(username=username, email=email, first_name=first_name, password=password, user_type=2)
            print("User >>",user)
        except Exception as err:
            print(err)
        print(user)
        try:
            print("adminuser",adminuser)
            staff = Staffs.objects.create(user=user,admin=adminuser)

            print("staff ",staff)
        except Exception as err:
            print(err)
        messages.success(request, "Successfully Added User ")
        return HttpResponseRedirect(reverse("add tester"))
    except Exception as e:
        print(e)  # Log the exception for debugging
        messages.error(request, "Failed to Add User")
        return HttpResponseRedirect(reverse("add tester"))
def edit_staff_save(request):
    staff_id = None
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user_id = request.POST.get("user_id")
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        username = request.POST.get("username")

        try:
            user = CustomUser.objects.get(id=user_id)
            staff_id = user.staff.id
            #print(type(staff_id))
            #print(staff_id)
            user.first_name = first_name
            user.email = email
            user.username = username
            user.save()

            #staff_model = Staffs.objects.get(admin=user)
            # Assuming you want to update the staff's information
            #staff_model.user = user
            #staff_model.save()

            messages.success(request, "Successfully Edited Staff")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id": staff_id}))
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id": staff_id}))
        except Staffs.DoesNotExist:
            messages.error(request, "Staff not found")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id": staff_id}))
        except Exception as e:
            messages.error(request, f"Failed to Edit Staff: {str(e)}")
            return HttpResponseRedirect(reverse("edit_staff", kwargs={"staff_id": staff_id}))


import pandas as pd
from django.http import HttpResponse
from .models import testcases


def download_user_stories(request):
    # Retrieve the test cases data
    test_cases = testcases.objects.all()

    # Prepare data for DataFrame
    data = []
    for tc in test_cases:
        data.append({
            'ID': tc.id,
            'Title User Story': tc.userstory_d.title if tc.userstory_d else '',
            'Title Test Cases': tc.title,
            'Description': tc.bady,
            'Tester': tc.staff_id.admin.first_name if tc.staff_id and tc.staff_id.admin else ''
        })

    # Create DataFrame
    df = pd.DataFrame(data)

    # Create a BytesIO buffer
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="user_stories.xlsx"'

    # Write the DataFrame to the buffer
    df.to_excel(response, index=False)

    return response
