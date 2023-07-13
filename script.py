# pip install beautifulsoup4
# pip install requests
# pip install requests



import argparse
import requests
from bs4 import BeautifulSoup

# Fonction pour extraire le contenu d'un site web
def extract_content(url, keywords):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Recherche des éléments pertinents en fonction des mots-clés
    relevant_elements = []
    for keyword in keywords:
        elements = soup.find_all(string=lambda string: keyword.lower() in string.lower())
        relevant_elements.extend(elements)

    return relevant_elements

# Fonction pour traiter et formater le contenu extrait
def process_content(content):
    processed_content = []
    for element in content:
        if isinstance(element, str):
            processed_content.append(element.strip())
        else:
            processed_content.append(element.text.strip())

    return processed_content

# Configuration des paramètres en ligne de commande
parser = argparse.ArgumentParser(description='Script d\'extraction de contenu web')
parser.add_argument('url', type=str, help='URL du site web à extraire')
parser.add_argument('--keywords', type=str, nargs='+', help='Mots-clés à rechercher')
parser.add_argument('--output', type=str, help='Chemin du fichier de sortie')

# Analyse des arguments en ligne de commande
args = parser.parse_args()

# Extraction du contenu en fonction de l'URL et des mots-clés fournis
content = extract_content(args.url, args.keywords)

# Traitement du contenu extrait
processed_content = process_content(content)

# Enregistrement du contenu dans un fichier texte ou affichage à la console
output_file = args.output
if output_file:
    with open(output_file, 'w') as file:
        for element in processed_content:
            file.write(element + '\n')
else:
    for element in processed_content:
        print(element)
