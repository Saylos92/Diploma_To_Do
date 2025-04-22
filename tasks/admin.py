from django.contrib import admin

from tasks.models import Task, Priority, Category

admin.site.register([Task, Priority, Category])
