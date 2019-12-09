from django.contrib import admin

# Register your models here.
from newsapp.models import News,Headnews
admin.site.register(News)
admin.site.register(Headnews)

