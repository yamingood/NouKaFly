# recherche/views_api.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import rechercher_hotels
import requests

@api_view(['GET'])
def api_recherche_hotels(request):
    destination = request.GET.get('destination')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')
    resultats = rechercher_hotels(destination, checkin, checkout)
    return Response(resultats.get('data', []))


# API pour rechercher une destination via Booking.com (RapidAPI)
@api_view(['GET'])
def api_recherche_destination(request):
    import requests

    destination = request.GET.get('query', 'Paris')

    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
    querystring = {"query": destination}
    headers = {
        "x-rapidapi-key": "e80213503amsh1e157337b89991cp123710jsn78f3e82d2846",
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return Response(response.json())


@api_view(['GET'])
def api_recherche_vols_destination(request):
    destination = request.GET.get('query', '')
    if not destination:
        return Response({"error": "Paramètre 'query' manquant"}, status=400)

    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchDestination"
    querystring = {"query": destination}
    headers = {
        "x-rapidapi-key": "e80213503amsh1e157337b89991cp123710jsn78f3e82d2846",
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    print("====== JSON reçu depuis l'API flights/searchFlights ======")
    print(response.text)  # Pas .json() ici pour éviter erreur si vide
    try:
        return Response(response.json())
    except Exception:
        return Response({"error": "Réponse invalide de l'API externe"}, status=502)