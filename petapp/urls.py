# from django.urls import path
# from . import views


# urlpatterns = [
# path('amin/',views.anim_view,name='anim_view')

# ]




from django.urls import path
from . import views

urlpatterns = [
    path('anim/', views.anim_create, name='anim_add'),   
    path('list/', views.anim_list, name='anim_list')  
]
