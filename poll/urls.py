from django.urls import path
from .import views
urlpatterns = [
    path('',views.polls,name='polls'),
    path('<int:id>/',views.details,name='details'),
    path('<int:id>/result/',views.result,name='result'),
    path('<int:id>/votes/',views.votes,name='votes'),

]