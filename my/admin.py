from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from my.models import CustomUser,Events,userstory,AdminHOD,Staffs,testcases
# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)
admin.site.register(Events)
admin.site.register(userstory)
admin.site.register(AdminHOD)
admin.site.register(Staffs)
admin.site.register(testcases)