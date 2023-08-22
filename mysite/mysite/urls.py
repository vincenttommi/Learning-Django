from django.contrib import admin
from  django.urls import include,path
#The include() function allows referencing other URLconfs

urlpatterns = [
    
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]