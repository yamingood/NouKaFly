# ✈️ NouKaFly

**NouKaFly** est un comparateur de vols interactif développé avec Django, qui utilise l’API de Booking.com via RapidAPI.  
Il permet de rechercher des vols entre deux destinations avec filtres, animations, détails enrichis et tri dynamique.

---

## 🚀 Fonctionnalités

- 🔍 Recherche de vols avec :
  - Pays de départ et d’arrivée (autocomplétion)
  - Sélection des dates aller/retour
  - Nombre d’adultes
  - Classe (Économie, Premium, Business, First)
- 🎛 Tri dynamique : `Best`, `Cheapest`, `Fastest`
- 📦 Détails complets de chaque vol (overlay)
  - Numéro du vol, horaires, durée, compagnie, bagages
  - Tarif détaillé, options flexibles, politique de remboursement
- 🌍 Intégration API Booking.com (RapidAPI)
- ✨ Interface responsive avec Bootstrap + animations AOS
- 🧠 Stockage temporaire des paramètres de recherche (évite de tout re-renseigner)

---

## 🧰 Technologies

- Python 3.10+  
- Django 4.x  
- HTML5 / CSS3 / Bootstrap 5  
- JavaScript (fetch, DOM, AOS, loader, overlay)
- API Booking.com (via [RapidAPI](https://rapidapi.com/DataCrawler/api/booking-com15/))

---

## ⚙️ Installation

1. **Clone du repo**
```bash
git clone https://github.com/yamingood/NouKaFly.git
cd NouKaFly```

2.	**Création d’un environnement virtuel**
python -m venv venv
source venv/bin/activate

