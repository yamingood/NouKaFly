from django.urls import path
from .views import rechercher_hotels_api
from NouKaFlyApp.viewsApi import api_recherche_vols_destination
from .views import details_vol


urlpatterns = [
    path('api/hotels/', rechercher_hotels_api),
    path('api/recherche-vols-destination/', api_recherche_vols_destination),
    path('api/details-vol/', details_vol, name="details_vol"),
]

