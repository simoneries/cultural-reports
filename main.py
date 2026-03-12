"""
Application visant à récupérer les principales expos en cours à Paris toutes les semaines

"""
import pandas as pd
import numpy as np
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from datetime import datetime
import json


#1 - Récuperer les principales expos à Paris dans une liste à print
expos_louvre = []
urlPM = "https://www.parismusees.paris.fr/fr/expositions"
urlL = "https://www.louvre.fr/expositions-et-evenements/expositions"

names = []
musees=[]
urls_expo = []
dates_debut = []
dates_fin = []

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
                names.append(name)
            except: 
                name = None
                names.append(name)
            
            try:
                url_expo = item.get_attribute("href")# Rajouter le reste de l'Url
                urls_expo.append(url_expo)
            except:
                url_expo = None
                urls_expo.append(url_expo)

            try: 
                musee = item.locator(".nom-musee").first.inner_text()
                musees.append(musee)
            except PlaywrightTimeoutError:
                musee = None
                musees.append(musee)

            try:
                date_debut_loc = item.locator(".date-debut-evenement").all_inner_texts()
                date_debut_str = date_debut_loc[0].replace("\n","-").replace("/","-")
                date_format = '%d-%m-%y'
                date_debut = datetime.strptime(date_debut_str,date_format)
                date_fin_loc = item.locator(".date-fin-evenement").all_inner_texts()
                date_fin_str = date_fin_loc[0].replace("\n","-").replace("/","-")
                date_format = '%d-%m-%y'
                date_fin = datetime.strptime(date_fin_str,date_format)

                dates_debut.append(date_debut)
                dates_fin.append(date_fin)

            except PlaywrightTimeoutError:
                date_debut = None
                date_fin = None
                dates_debut.append(date_debut)
                dates_fin.append(date_fin)
            
            #Next step récupérer les jours, le musée 
            #Step - Passer les données dans un DataFrame
        browser.close()


def get_louvre(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url,timeout=0)
        count = page.locator("#exposition-d-actualite a").count()
        
        for i in range(count):
            try:
                item = page.locator("#exposition-d-actualite a").nth(i)
                data_tracking_str = item.get_attribute("data-tracking")  
                data_dict = json.loads(data_tracking_str)
                names.append(data_dict["label"])
            except PlaywrightTimeoutError:
                name = None
                names.append(name)

get_louvre(urlL)




#get_paris_musees(urlPM)


df = pd.DataFrame({"musee":musees,"nom":names,"debut":dates_debut,"fin":dates_fin,"url":urls_expo})






# 2 - Set up les données dans un DataFrame
