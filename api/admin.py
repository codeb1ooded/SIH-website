from django.contrib import admin
from .models import *

admin.site.register(Teacher)
admin.site.register(Education)
admin.site.register(Teacher_Education)
admin.site.register(Attendance_Present)
admin.site.register(Attendance_Holiday)
