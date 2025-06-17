<div id="top">

<!-- EN-TÊTE STYLE : CLASSIQUE -->
<div align="center">

# NOUKAFLY

<em>Réinventer la planification de voyages grâce à une innovation fluide</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/last-commit/yamingood/NouKaFly?style=flat&logo=git&logoColor=white&color=0080ff" alt="Dernier commit">
<img src="https://img.shields.io/github/languages/top/yamingood/NouKaFly?style=flat&color=0080ff" alt="Langage principal">
<img src="https://img.shields.io/github/languages/count/yamingood/NouKaFly?style=flat&color=0080ff" alt="Nombre de langages">

<em>Créé avec :</em>

<img src="https://img.shields.io/badge/Markdown-000000.svg?style=flat&logo=Markdown&logoColor=white" alt="Markdown">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">

</div>
<br>

---

## 📄 Table des matières

- [Présentation](#-présentation)
- [Démarrage rapide](#-démarrage-rapide)
    - [Prérequis](#-prérequis)
    - [Installation](#-installation)
    - [Utilisation](#-utilisation)
    - [Tests](#-tests)
- [Fonctionnalités](#-fonctionnalités)
- [Structure du projet](#-structure-du-projet)
- [Remerciements](#-remerciements)

---

## ✨ Présentation

**NouKaFly** est une plateforme web de comparaison de vols et hôtels open-source, construite avec Django et intégrée aux API de Booking.com via RapidAPI. Elle permet à l’utilisateur de rechercher, filtrer et visualiser les options de voyage avec des données actualisées en temps réel.

### 🧠 Pourquoi NouKaFly ?

- 🔧 **Architecture modulaire** : Vue claire entre les modèles, vues, et API, facilitant l'extension.
- 🌐 **Données en temps réel** : Requêtes dynamiques pour les vols et hôtels via API externes.
- 🖥️ **Interface responsive** : Champs de recherche animés, filtres de tri, et design moderne.
- 🔒 **Prête à être déployée** : Compatible WSGI & ASGI.
- 🧭 **Gestion facile** : Interface admin Django intégrée pour la gestion des requêtes.

---

## 📌 Fonctionnalités

|      | Composant       | Détails                                                                                     |
| :--- | :-------------- | :------------------------------------------------------------------------------------------ |
| ⚙️  | **Architecture**  | Django MVC, code structuré et évolutif                                                     |
| 📦 | **API Intégrées** | Booking.com (vols, hôtels, destinations) via RapidAPI                                     |
| 🎨 | **UX/UI**         | Design moderne avec Bootstrap 5, animations avec AOS.js, et icônes Bootstrap Icons         |
| 🔍 | **Filtres dynamiques** | Classe cabine (éco, business, etc.), tri des résultats (meilleur, moins cher, plus rapide) |
| 🧳 | **Détails du vol** | Overlays avec numéro de vol, bagages, correspondances, politiques tarifaires, etc.         |
| 💾 | **Stockage temporaire** | Champs pré-remplis après recherche, historique en session                               |

---

## 📁 Structure du projet

```sh
└── NouKaFly/
    ├── NouKaFly            # Configuration principale Django
    ├── NouKaFlyApp         # Application : vues, utils, templates
    │   ├── static/images   # Logos, animations loader, icônes
    │   ├── templates       # HTML : accueil, recherche, détails
    │   ├── views.py        # Vue principale de recherche de vol
    │   ├── viewsApi.py     # Endpoints REST
    │   ├── utils.py        # Fonctions de requêtes API
    └── manage.py

```
## 🚀 Démarrage rapide

### 📋 Prérequis
	•	Python ≥ 3.8
	•	pip ou conda
	•	Compte RapidAPI avec clé valide

### ⚙️ Installation
```sh
# 1. Cloner le dépôt
$ git clone https://github.com/yamingood/NouKaFly.git
$ cd NouKaFly

# 2. Créer un environnement virtuel
$ python -m venv venv
$ source venv/bin/activate  # ou .\\venv\\Scripts\\activate sous Windows

# 3. Installer les dépendances
$ pip install -r requirements.txt

# 4. Lancer le serveur
$ python manage.py runserver
```

### 💻 Utilisation
	•	Accès : http://127.0.0.1:8000/
	•	Page d’accueil = formulaire de recherche de vols avec autocomplétion

### 🧪 Tests

⚠️ Les tests unitaires ne sont pas encore disponibles.

## ❤️ Remerciements
	•	API : Booking.com API - via RapidAPI
	•	Framework : Django
	•	UI : Bootstrap 5, AOS.js, Bootstrap Icons

<div align="left"><a href="#top">⬆ Revenir en haut</a></div>

