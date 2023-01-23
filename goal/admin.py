from django.contrib import admin
from .models import Blog, Room, Messages, Students

# Register your models here.
admin.site.register(Blog)
admin.site.register(Room)
admin.site.register(Messages)
admin.site.register(Students)


