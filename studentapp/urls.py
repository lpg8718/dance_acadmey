from  django.urls import path
from . import views
urlpatterns = [
   path('',views.studenthome),
   path('updateprofile/',views.updateprofile),
   path('student_course_list/',views.student_course_list),
   path('student_batch_list/',views.student_batch_list),
   path('select_batch/',views.select_batch),
   path('logout1/',views.logout1),
   path('enroll_batch/',views.enroll_batch),
   path('profile/',views.profile),
   path('gallery1/',views.gallery1),
]