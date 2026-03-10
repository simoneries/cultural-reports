"""
Application visant à récupérer les principales expos en cours à Paris toutes les semaines

"""
from playwright.sync_api import sync_playwright


#1 - Récuperer les principales expos à Paris dans une liste à print
expos_louvre = []
urlPM = "https://www.parismusees.paris.fr/fr/expositions"

#1 - A - Récupérer les données du Louvre

def get_paris_musees(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        name = page.locator(".view-content .title").all_inner_texts()
        print(name)

        browser.close()

get_paris_musees(urlPM)



#1 - B - Récupérer les données de plusieurs musées
# 2 - Set up les données dans un DataFrame
