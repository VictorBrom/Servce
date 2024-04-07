from django.urls import path, include
from . import views
from django.views.generic import View
urlpatterns = [
    path('', views.partners_index),
    path('create_contracts', views.PartnerContracts.as_view()),
    path('<int:id_partner>', views.contract_index),
    path('create_partner', views.PartnerIndex.as_view()),
]