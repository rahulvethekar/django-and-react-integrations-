from django.urls import path
from .views import StudentListCreate,UpdateStudent,StudentById

urlpatterns = [
    path('student/',StudentListCreate.as_view(),name='student'),
    path('updatestudent/<int:pk>',UpdateStudent.as_view(),name='updatestudent'),
    path('studentbyid/<int:rn>',StudentById.as_view(),name='studentbyid'),

]