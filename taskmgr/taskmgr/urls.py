from django.contrib import admin
from django.urls import path, include

admin.site.site_title = "Admin Page"
admin.site.site_header = "Task Manager Admin Page"
admin.site.index_title = "Task Manager"

urlpatterns = [
    path('', include('mainpages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')), 
]
