from django.urls import path
from . import views
from baobah.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name = 'index'),
    path('upload/', views.upload, name = 'upload-oas'),
    path('update/<int:oas_id>', views.update_oas),
    path('delete/<int:oas_id>', views.delete_oas)
]
#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
