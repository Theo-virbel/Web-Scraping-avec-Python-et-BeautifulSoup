import requests
from bs4 import BeautifulSoup

# URL du site
url = "https://pythonjobs.github.io/"

# Récupérer le contenu de la page
response = requests.get(url)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Parser le contenu HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Trouver tous les blocs d'offres d'emploi
    job_listings = soup.find_all("div", class_="job")
    
    # Boucle pour afficher les informations de chaque offre d'emploi
    for job in job_listings:
        title = job.find("h1").text.strip()  # Titre de l'offre
        location = job.find("span", class_="info").text.strip()  # Localisation
        
        # Rechercher le nom de l'entreprise et gérer le cas où il n'est pas trouvé
        company = job.find("h2")  # Nom de l'entreprise
        if company:  # Vérifie si l'élément existe
            company = company.text.strip()
        else:
            company = "Non spécifié"  # Valeur par défaut si non trouvé

        # Trouver la description, gérer également le cas où elle n'est pas trouvée
        description = job.find("div", class_="description")
        if description:  # Vérifie si l'élément existe
            description = description.text.strip()
        else:
            description = "Non spécifiée"  # Valeur par défaut si non trouvé
        
        # Afficher les résultats
        print(f"Titre : {title}")
        print(f"Entreprise : {company}")
        print(f"Localisation : {location}")
        print(f"Description : {description}\n")
else:
    print(f"Erreur lors de la récupération de la page : {response.status_code}")
