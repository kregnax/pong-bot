from bs4 import BeautifulSoup
import requests
import re
import json

def get_hero_list():
    '''Returns a list of current heroes from battlenet'''
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

def get_hero_patch_notes(hero, next_cmd=False):
    '''Input a hero name and return a scraped list of the last change notes for that hero. Might add next note funcaitonality'''
    if hero.lower() in get_hero_list():
        url = "https://heroespatchnotes.com/hero/{}.html".format(hero) #abathur.html#patch2017-09-26"
        page = requests.get(url, verify=False)
        soup = BeautifulSoup(page.text, 'html.parser')
        notes_list = []
        for elem in soup.find("div", class_="panel panel-primary").find_all("li"):
            notes_list.append(elem.get_text())
    return notes_list