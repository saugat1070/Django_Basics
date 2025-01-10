from django.contrib import admin
from FirstApp.models import Employee
from FirstApp.models import StudentInfo
from FirstApp.models import PhotoFromExternal
from FirstApp.models import form_submission
# Register your models here.
class EmpolyeeAdmin(admin.ModelAdmin):
    #modelname_Admin() fixed not to be changed
    list_display = ['id_no','name','salary','address']


class StudentInfoAdmin(admin.ModelAdmin):
    #modelname_Admin() fixed not to be changed
    list_display = ['id_no','name','clss_no','Mark']



class form_submissionAdmin(admin.ModelAdmin):
    list_display = ['user_name','user_password']


admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.register(PhotoFromExternal)
admin.site.register(form_submission)
admin.site.register(Employee,EmpolyeeAdmin)
