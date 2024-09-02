from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


class LoginCheckMiddleWare(MiddlewareMixin):

    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        user=request.user
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "my.productownerViews":
                    pass
                elif modulename == "my.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("index"))
            elif user.user_type == "2":
                if modulename == "my.testerViews":
                    pass
                elif modulename == "my.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("tester"))
            else:
                return HttpResponseRedirect(reverse("login"))

        else:
            if request.path == reverse("login") or request.path == reverse("dologin") or modulename == "my.views" :
                pass
            else:
                return HttpResponseRedirect(reverse("login"))