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
        
        # Rechercher le nom de l'entreprise via la classe "i-company"
        company_tag = job.find("i", class_="i-company")
        if company_tag:
            company = company_tag.find_next_sibling(text=True).strip()
        else:
            company = "Non spécifié"  # Si l'entreprise n'est pas trouvée

        # Rechercher la description spécifique dans <p class="detail">
        description = job.find("p", class_="detail")
        if description:
            description = description.text.strip()  # Récupérer la description complète
        else:
            description = "Non spécifiée"  # Valeur par défaut si non trouvée
        
        # Afficher les résultats
        print(f"Titre : {title}")
        print(f"Entreprise : {company}")
        print(f"Localisation : {location}")
        print(f"Description : {description}\n")
else:
    print(f"Erreur lors de la récupération de la page : {response.status_code}")
