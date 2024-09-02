from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Staff"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)
    def __str__(self):
        return self.first_name
class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="adminep")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return str(self.id)
class Staffs(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name="staff")
    admin=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,related_name="staffs")
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    objects=models.Manager()

    def __str__(self):
        return str(self.id)
class userstory(models.Model):
    id=models.AutoField(primary_key=True)
    admin = models.ForeignKey("AdminHOD", on_delete=models.PROTECT, blank=True, null=True)
    title=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    objects=models.Manager()
    staff=models.ForeignKey("Staffs",on_delete=models.PROTECT,blank=True,null=True)
    active= models.BooleanField(default=False)

    def __str__(self):
        return self.title


class testcases(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    userstory_d = models.ForeignKey("userstory", on_delete=models.PROTECT, blank=True, null=True)
    staff_id=models.ForeignKey("Staffs",on_delete=models.PROTECT,blank=True,null=True)
    bady=models.CharField(max_length=255)
    objects=models.Manager()

    def __str__(self):
        return self.title




@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)



class Events(models.Model):
    admin = models.ForeignKey("AdminHOD", on_delete=models.PROTECT, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = "tblevents"

