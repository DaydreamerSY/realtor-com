from django.contrib import admin
from .models import Region, RealEstatePost, Member, Comment

# Register your models here.

admin.site.register(Region)
admin.site.register(RealEstatePost)
admin.site.register(Member)
admin.site.register(Comment)