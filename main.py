"""
Application visant à récupérer les principales expos en cours à Paris toutes les semaines

"""
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


#1 - Récuperer les principales expos à Paris dans une liste à print
expos_louvre = []
urlPM = "https://www.parismusees.paris.fr/fr/expositions"

#1 - A - Récupérer les données du Louvre

def get_paris_musees(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        count = page.locator(".view-content a").count()

        for i in range(count):
            item = page.locator(".view-content a").nth(i)
            name = item.get_attribute("title")
            urlPM = item.get_attribute("href")# Rajouter le reste de l'Url

            try: 
                musee = item.locator(".nom-musee").first.inner_text()
            except PlaywrightTimeoutError:
                musee = "Musee inconnu"
            

            print(name,urlPM,musee)
            
            #Next step récupérer les jours, le musée 
            #Step - Passer les données dans un DataFrame

        

        browser.close()

get_paris_musees(urlPM)





#1 - B - Récupérer les données de plusieurs musées
# 2 - Set up les données dans un DataFrame
