from django.views.generic import TemplateView
from django.urls import path

from .views import japanDashboard, numberOfForeignToJapan

urlpatterns = [
    # path('facts-about-aodp/', TemplateView.as_view(template_name="aodp.html")),
    path('japanDashboard/', japanDashboard, name='japanDashboard'),
    path('number_foreign2Japan', numberOfForeignToJapan, name='number_foreign2Japan')
]
