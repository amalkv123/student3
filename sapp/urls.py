from django.urls import path 
from sapp import views


urlpatterns = [

    path('',views.student, name='student'),
    path('add_students_data',views.add_students_data , name='add_students_data'),
    path('show',views.show , name='show'),
    path('editpage/<int:pk>',views.editpage , name="editpage"),
    path('editstudent_data/<int:pk>',views.editstudent_data , name='editstudent_data'),
   # path('delete/<int:pk>',views.delete , name='delete'),
    path('delete_product/<int:pk>',views.delete_product ,  name='delete_product'),
    path('detailview/<int:pk>',views.detailview , name='detailview')

]


     