
# import .views

from . import views
from django.contrib import admin
from django.urls import path
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home),
    path('upload',views.upload),
    path("bin",views.getBinInformation)
]
