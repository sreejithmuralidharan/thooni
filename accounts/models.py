
from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from social_analytics import settings
from django.urls import reverse
from guardian.shortcuts import assign_perm

class Profile(models.Model):
    user                    =       models.OneToOneField(User, on_delete=models.CASCADE)
    full_name               =       models.CharField(max_length=100)
    address1                =       models.CharField(verbose_name='Street address', max_length=150,null=True, blank=True)
    address2                =       models.CharField(verbose_name='Address 2', max_length=150, blank=True, null=True)
    locality                =       models.CharField(verbose_name='City/Town', max_length=50, null=True, blank=True)
    region                  =       models.CharField(verbose_name='State/Province/County', max_length=50, null=True, blank=True)
    postal_code             =       models.CharField(verbose_name='Zip/Postal code', max_length=50, null=True, blank=True)
    country                 =       CountryField('Country', null=True, blank=True)
    phone_number            =       PhoneNumberField(null=True, blank=True)
    email                   =       models.EmailField(null=True, blank=True)
    image                   =       models.ImageField(upload_to='profile_pics',blank=True, null=True)
    created_on              =       models.DateTimeField(auto_now_add=True)
    modified_on             =       models.DateTimeField(auto_now=True)

    class Meta:
        default_permissions = ('add', 'change', 'delete')
        permissions = (
            ('view_profile', 'Can view profile'),
        )

    def __str__(self): 
        return self.user.username
    
    def get_absolute_url(self):
        return reverse("accounts:profile-detail", kwargs={"pk": self.pk})
    
    @property
    def profile_picture(self):
        if self.image:
            return self.image.url
        else:
            return '/static/profile_pics/profile_pic_placeholder.png'
    
    
        

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    
    if created and instance.username != settings.ANONYMOUS_USER_NAME:
        profile = Profile.objects.create(pk=instance.pk, user=instance)
        assign_perm("change_user", instance, instance)
        assign_perm('view_profile', instance, profile)
        assign_perm('change_profile', instance, profile)
        assign_perm('delete_profile', instance, profile)
    try:
        instance.profile.save()
    except Exception as e:
        print(e)