# recherche/utils.py
import requests

RAPIDAPI_KEY = "Te80213503amsh1e157337b89991cp123710jsn78f3e82d2846"

def rechercher_hotels(destination, checkin, checkout):
    url = "https://booking-com15.p.rapidapi.com/api/v1/hotels/searchHotels"
    querystring = {
        "destination": destination,
        "checkin_date": checkin,
        "checkout_date": checkout,
        "adults": "2",
        "room_qty": "1"
    }

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()