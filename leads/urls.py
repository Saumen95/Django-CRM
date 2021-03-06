from django.urls import path
from .views import lead_list, lead_details, lead_create,lead_update, lead_delete

app_name = "leads"

urlpatterns = [
    path('', lead_list, name='lead-list'),
    path('int:<pk>/', lead_details, name='lead-details'),
    path("create/", lead_create,name='lead-create'),
    path('int:<pk>/update/',name='lead-update'),
    path('int:<pk>/delete/', lead_delete, name='lead-delete'),
]
