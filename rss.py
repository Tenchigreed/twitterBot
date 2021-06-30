import feedparser
import requests
from requests.exceptions import HTTPError

def checkUrl(url):
    urlString = url
    try:
        r = requests.get(urlString)
        r.raise_for_status()
    except :
        return False
    else:
        return True

def mois (dateMois):
    if dateMois == "Jan":
        return '01'
    elif dateMois == "Feb":
        return '02'
    elif dateMois == "Mar":
        return '03'
    elif dateMois == "Apr":
        return '04'
    elif dateMois == 'May':
        return '05'
    elif dateMois == 'Jun':
        return '06'
    elif dateMois == 'Jul':
        return '07'
    elif dateMois == 'Aug':
        return '08'
    elif dateMois == 'Sep':
        return '09'
    elif dateMois == 'Oct':
        return '10'
    elif dateMois == 'Nov':
        return '11'
    elif dateMois == 'Dec':
        return '12'
    else:
        return '99'

def annee (dateAnnee):
    anneeTemp = dateAnnee[2] + dateAnnee[3]
    return anneeTemp

def heure (dateHeure):
    heureTemp = dateHeure[0] + dateHeure[1]
    return heureTemp

def fluxRSS(url): 
    check = checkUrl(url)
    if check == True:    
        feed = feedparser.parse(url)
        
        entry = feed.entries
        
        titre = entry[0]['title']
        lien = entry[0]['link']
        dateBrute = entry[0]['published']
        
        dateBrute = dateBrute.split(" ")
        moisDate = mois(dateBrute[2])
        anneeDate = annee(dateBrute[3])
        heureDate = heure(dateBrute[4])
        
        date = dateBrute[1] + moisDate + anneeDate + heureDate
        
        return date, titre, lien
    else :
        return 0 , 0 , 0 , 0


def fluxRSSPeer(url, auteur):
    check = checkUrl(url)
    if check == True:
        feed = feedparser.parse(url)
        
        entry = feed.entries
        
        for data in entry:
            titre = data['title']
            lien = data['link']
            dateBrute = data['published']
            
            dateBrute = dateBrute.split(" ")
            moisDate = mois(dateBrute[2])
            anneeDate = annee(dateBrute[3])
            heureDate = heure(dateBrute[4])
            
            date = dateBrute[1] + moisDate + anneeDate + heureDate
            author = data["author"]
            if author == auteur:
                dateFinal = date 
                titreFinal = titre
                lienFinal = lien
                return dateFinal, titreFinal, lienFinal 
            else :
                return 0, 0, 0
    else :
        return 0 , 0 , 0
