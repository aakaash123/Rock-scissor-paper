from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('rock/',views.rock,name='rock'),
    path('paper/',views.paper,name='paper'),
    path('scissor/',views.scissor,name='scissor'),
    # path('result/',views.result,name='result'),
]
