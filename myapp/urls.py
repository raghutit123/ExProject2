from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOverview, name='apiOverview'),
    path('student-all/', views.StudentAll, name='studentall'),
    path('student-list/<int:pk>/',views.StudentList, name='studentlist'),

]