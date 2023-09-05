from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'tracker'  # Assuming you have defined this in your app's urls.py

urlpatterns = [
    path('', views.weight_form_view, name='trackerindex'),
    path('update/<int:entry_id>/', views.update_weight_view, name='update'),
    path('delete/<int:entry_id>/', views.delete_weight_view, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)