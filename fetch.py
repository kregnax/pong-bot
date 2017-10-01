from bs4 import BeautifulSoup
import requests
import re
import json

def get_hero_list():
    url = "http://us.battle.net/heroes/en/heroes/#/"
    page = requests.get(url, verify=False)
    soup = BeautifulSoup(page.text, 'html.parser')
    for cd in soup.findAll(text=True):
        if "window.heroes" in cd:
            cd = cd.split(".heroes = ")[1]
            heroes = cd.split(";\n")[0]
            continue
    hero_json = json.loads(heroes)
    hero_list = []
    for elem in hero_json:
         hero_list.append(elem['analyticsName'])
    return hero_list
