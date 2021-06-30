import feedparser
import requests
from requests.exceptions import HTTPError

def annee (anneeTemp):
    anneeDate = anneeTemp[2] + anneeTemp[3]
    return anneeDate

def mois (moisTemp):
    moisDate = moisTemp[5] + moisTemp[6]
    return moisDate

def jour (jourTemp):
    jourDate = jourTemp[8] + jourTemp[9]
    return jourDate


def heure (heureTemps):
    heureDate = heureTemps[11] + heureTemps[12]
    return heureDate

def checkUrl(url):
    urlString = url
    try:
        r = requests.get(urlString)
        r.raise_for_status()
    except :
        return False
    else:
        return True


def youtube(url):
    url = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + url
    check = checkUrl(url)
    if check == True:    
        feed = feedparser.parse(url)
        
        entry = feed.entries
        date = entry[0]['published']
        link = entry[0]['link']
        dateAnnee = annee(date)
        dateMois = mois(date)
        dateJour = jour(date)
        dateHeure = heure(date)
        date = dateJour + dateMois + dateAnnee + dateHeure
        if int(date[0]) == 0:
            date = int(date) + 2
            date = '0' + str(date)
        else:
            date = int(date) + 2
        
        return date, link
    else :
        return 0 , 0


