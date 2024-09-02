"""
URL configuration for mary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from mary import settings
from my import views,testerViews,productownerViews


urlpatterns = [
    path('admin/', admin.site.urls),
   path('', views.home,name="home"),
   path('tester', testerViews.tester,name="tester"),
   path('login', views.showloginPage,name="login"),
   path('error-403', views.hidden, name="error-403"),
path('delete_story/<int:pk>/', productownerViews.delete_story, name="delete_story"),
path('delete/<int:pk>/', productownerViews.delete_staff_instance, name="delete"),
   path('view-user stories/', productownerViews.viewtesters, name="view-user stories"),
path('view-user_storie', testerViews.testerview, name="view-user storie"),
   path('view-tester', productownerViews.viewteste, name="view-tester"),
   path('edit_staff/<int:staff_id>', productownerViews.edit_staff, name="edit_staff"),
   path('edit_user_story/<int:staff_id>', productownerViews.edit_user, name="edit_user_story"),
   path('add tester', productownerViews.addtester,name="add tester"),
   path('add_user_story', productownerViews.add_user, name="add_user_story"),
   path('viewtest_case', productownerViews.viewtest_case, name="viewtest_case"),
   path('download_user_stories', productownerViews.download_user_stories, name="download_user_stories"),



   path('add', productownerViews.user_story, name="add"),
   path('add_staff_save',productownerViews.add_staff_save, name="add_staff_save"),
   path('edit_staff_save', productownerViews.edit_staff_save, name="edit_staff_save"),
   path('singup', views.singup, name="singup"),
   path('signup_user', views.signup_user, name="signup_user"),
   path('dologin', views.dologin,name='dologin'),
   path('index',productownerViews.index, name='index'),
   path('all_events/', productownerViews.all_events, name='all_events'),
   path('add_event/', productownerViews.add_event, name='add_event'),
   path('update/', productownerViews.update, name='update'),
   path('remove/', productownerViews.remove, name='remove'),
   path('get_user', views.GetUserDetails),
   path('logout_user', views.logout_user,name='logout_user' ),
   path('all_event/', testerViews.all_event, name='all_event'),
   path('update_event/', testerViews.update_event, name='update_event'),
   path('y_testcases/', testerViews.y_testcases, name='y_testcases'),
   path('add_testcase', testerViews.add_testcase, name='add_testcase'),

   path('viwer_testcases', testerViews.viwer_testcases, name='viwer_testcases'),



]
