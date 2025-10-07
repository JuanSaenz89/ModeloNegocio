from django.urls import path
from .views import pages

urlpatterns = [
    path('<int:page_id>/<slug:page_title>', pages, name='pages'),
]