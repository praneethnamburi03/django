from . import views
from django.urls import path
app_name='new1'

urlpatterns = [
    #path('',views.view,name='view'),
    path('',views.IndexClassView.as_view(),name='view'),
    #new1/1
    #path('<int:id1>/',views.studentid,name='studentid'),
    path('<int:pk>/',views.detailOfStudent.as_view(),name='studentid'),
    path('newone/',views.newone,name='newone'),
    #add student
    path('add',views.newstudent,name='newstudent'),
    #path('add',views.CreateStudent.as_view(),name='newstudent'),
    #edit the student
    path('edit/<int:id>',views.editstudent,name='editstudent'),
    #delete 
    path('delete/<int:id>',views.deletestudent,name='deletestudent'),
]


