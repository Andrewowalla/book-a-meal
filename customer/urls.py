from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('confirmation/',views.post,name='confirmation')
]
+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
