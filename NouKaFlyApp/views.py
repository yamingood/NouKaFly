from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import rechercher_hotels
import requests
from datetime import datetime



def accueil(request):
    context = {}
    if request.method == 'POST':
        destination = request.POST['destination']
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        resultats = rechercher_hotels(destination, checkin, checkout)
        context = {
            'resultats': resultats.get('data', []),
            'destination': destination
        }
    return render(request, 'recherche/accueil.html', context)

@api_view(['GET'])
def rechercher_hotels_api(request):
    destination = request.GET.get('destination')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')

    if not destination or not checkin or not checkout:
        return Response({"error": "destination, checkin et checkout sont requis."}, status=400)

    data = rechercher_hotels(destination, checkin, checkout)
    return Response(data)

def recherche_destination_view(request):
    import requests

    resultats = []
    query = ''
    if request.method == 'POST':
        query = request.POST.get('query', '')
        if query:
            url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchDestination"
            headers = {
                "x-rapidapi-key": "e80213503amsh1e157337b89991cp123710jsn78f3e82d2846",
                "x-rapidapi-host": "booking-com15.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params={"query": query})
            resultats = response.json().get('data', [])

    return render(request, 'recherche/recherche_destination.html', {'resultats': resultats, 'query': query})

def recherche_vols_destination_view(request):
    vols = []
    erreur = None
    from_query = ''
    to_query = ''
    date_depart = ''
    date_retour = ''
    nb_adultes = '1'
    cabin_class = ''
    from_id = None
    to_id = None
    sort = 'BEST'
    if request.method == 'POST':
        from_id = request.POST.get('from_query_id')
        to_id = request.POST.get('to_query_id')
        date_depart = request.POST.get('date_depart')
        date_retour = request.POST.get('date_retour')
        nb_adultes = request.POST.get('nb_adultes', '1')
        cabin_class = request.POST.get('cabin_class', 'ECONOMY')
        sort = request.POST.get('sort', 'BEST')
        from_query = request.POST.get('from_query')
        to_query = request.POST.get('to_query')
        page = request.POST.get('page', '1')

        try:
            date_depart = datetime.strptime(date_depart, "%Y-%m-%d").date().isoformat()
            date_retour = datetime.strptime(date_retour, "%Y-%m-%d").date().isoformat()
        except (ValueError, TypeError):
            erreur = "Les dates saisies sont invalides. Veuillez réessayer."

        print("==== PARAMÈTRES DE RECHERCHE ====")
        print(f"From ID: {from_id}, To ID: {to_id}, Date de départ: {date_depart}, Date de retour: {date_retour}, Nombre d'adultes: {nb_adultes}")
        if from_id and to_id:
            url = "https://booking-com15.p.rapidapi.com/api/v1/flights/searchFlights"
            querystring = {
                "fromId": from_id,
                "toId": to_id,
                "departDate": date_depart,
                "returnDate": date_retour,
                "stops": "none",
                "pageNo": page,
                "adults": nb_adultes,
                "cabinClass": cabin_class,
                "sort": sort,
                "currency_code": "EUR"
            }
            headers = {
                "x-rapidapi-key": "e80213503amsh1e157337b89991cp123710jsn78f3e82d2846",
                "x-rapidapi-host": "booking-com15.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, params=querystring)
            if response.status_code == 200:
                json_data = response.json()
                data = json_data.get("data", {})
                vols = data.get("flightOffers", [])
                print("==== DONNÉES DES VOLS ====")
                print(json_data)
            else:
                erreur = "Erreur lors de la récupération des vols. Veuillez réessayer."

    return render(request, 'recherche/recherche_vols_destination.html', {
        "from_query": from_query,
        "to_query": to_query,
        "from_query_id": from_id,
        "to_query_id": to_id,
        "date_depart": date_depart,
        "date_retour": date_retour,
        "vols": vols,
        "sort": sort,
        "nb_adultes": nb_adultes,
        "cabin_class": cabin_class,
        "erreur": erreur
    })

@api_view(['GET'])
def details_vol(request):
    token = request.GET.get("token")
    if not token:
        return Response({"status": False, "message": "Token manquant."}, status=400)

    url = "https://booking-com15.p.rapidapi.com/api/v1/flights/getFlightDetails"
    headers = {
        "x-rapidapi-key": "e80213503amsh1e157337b89991cp123710jsn78f3e82d2846",
        "x-rapidapi-host": "booking-com15.p.rapidapi.com"
    }
    querystring = {"token": token, "currency_code": "EUR"}

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return Response(response.json())
    else:
        return Response({"status": False, "message": "Erreur lors de la récupération des détails du vol."}, status=500)