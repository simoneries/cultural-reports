"""
Application visant à récupérer les principales expos en cours à Paris toutes les semaines

"""
import pandas as pd
import numpy as np
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from datetime import datetime


#1 - Récuperer les principales expos à Paris dans une liste à print
expos_louvre = []
urlPM = "https://www.parismusees.paris.fr/fr/expositions"

#1 - A - Récupérer les données du Louvre

def get_paris_musees(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url,timeout=0)
        count = page.locator(".view-content a").count()

        for i in range(count):
            item = page.locator(".view-content a").nth(i)
            try: 
                name = item.get_attribute("title")
            except: 
                name = None
            
            try:
                url_expo = item.get_attribute("href")# Rajouter le reste de l'Url
            except:
                url_expo = None

            try: 
                musee = item.locator(".nom-musee").first.inner_text()
            except PlaywrightTimeoutError:
                musee = None

            try:
                date_debut_loc = item.locator(".date-debut-evenement").all_inner_texts()
                date_debut_str = date_debut_loc[0].replace("\n","-").replace("/","-")
                date_format = '%d-%m-%y'
                date_debut = datetime.strptime(date_debut_str,date_format)
                date_fin_loc = item.locator(".date-fin-evenement").all_inner_texts()
                date_fin_str = date_fin_loc[0].replace("\n","-").replace("/","-")
                date_format = '%d-%m-%y'
                date_fin = datetime.strptime(date_fin_str,date_format)

            except PlaywrightTimeoutError:
                date_debut = None
                date_fin = None

            print(name, url_expo, musee, date_debut,date_fin)
            
            #Next step récupérer les jours, le musée 
            #Step - Passer les données dans un DataFrame

        

        browser.close()

get_paris_musees(urlPM)





#1 - B - Récupérer les données de plusieurs musées
# 2 - Set up les données dans un DataFrame
