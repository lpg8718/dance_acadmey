from  django.urls import path
from django.conf.urls.static import static

from my1 import settings
from . import views

urlpatterns = [
    path('',views.adminhome),
    path('addcourse/',views.addcourse),
    path('addbatch/',views.addbatch),
    path('addstudent/',views.addstudent),
    path('courselist/',views.courselist),
    path('batchlist/',views.batchlist),
    path('course_update/',views.course_update),
    path('course_update_record/',views.course_update_record),
    path('course_delete/',views.course_delete),
    path('batch_update/',views.batch_update),
    path('batch_update_record/',views.batch_update_record),
    path('batch_delete/',views.batch_delete),
    path('studentlist/',views.studentlist),
    path('student_update/',views.student_update),
    path('student_update_record/',views.student_update_record),
    path('admin_update_profile/',views.admin_update_profile),
    path('contect/',views.contect),
    path('logout1/',views.logout1),
    path('student_delete/',views.student_delete),
    path('delstudent/',views.delstudent),
    path('delcourse/',views.delcourse),
    path('delbatch/',views.delbatch),
    path('image_upload/',views.image_upload),
    path('image_show/',views.image_show),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)