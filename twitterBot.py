# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:37:44 2021

@author: tenchi
"""
from youtube import youtube
from rss import fluxRSS
from rss import fluxRSSPeer
from datetime import datetime
import csv
import auth
import time

dico = {}
i=0
nom = 'site'

api, auth = auth.auth()

def formatageDate (actualDate):
    if int(actualDate[11:13]) <= 23:
        date = actualDate[8:10] + actualDate[5:7] + actualDate[2:4] + actualDate[11:13]
    elif int(actualDate[11:13]) == 23:
        date = actualDate[8:10] + actualDate[5:7] + actualDate[2:4] + "24"
    return date

def hashtagMulti (hashtag):
    hashtag = hashtag.split(":")
    hashtag = " #".join(hashtag)            
    return hashtag


dateReel = formatageDate(str(datetime.now()))
with open('info.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        placement = nom + str(i)
        dico[placement]= row
        i = i + 1

                
for site in dico:
    time.sleep(1)
    date = 0
    if dico[site][0] == "site":
        date, titre, lien = fluxRSS(dico[site][3])
        print(date)
        print(dico[site][1])
        hashtag = " #" + hashtagMulti(dico[site][4])
        if dico[site][2] != " ": 
            twitterUser = " @" + dico[site][2]
        elif dico[site][2] == " ":
            twitterUser = " "       
        if int(dateReel) - 3 == int(date):
            aTweeter = "Bonjour, un nouvel article est sortie sur le site : " + str(dico[site][1]) + ',  disponible maintenant ici : ' + str(lien) + str(hashtag) + str(twitterUser) + "\n"
            api.update_status(aTweeter)
            time.sleep(60)
        
    elif dico[site][0] == "youtube":
        date , lien = youtube(dico[site][3])
        print(date)
        print(dico[site][1])
        hashtag = " #" + hashtagMulti(dico[site][4])
        if dico[site][2] != " ": 
            twitterUser = " @" + dico[site][2]
        elif dico[site][2] == " ":
            twitterUser = " "         
        if int(dateReel) - 1 == int(date):
            aTweeter = "Bonjour, une nouvelle video est sortie sur la chaine #youtube : "+ str(dico[site][1])+ ',  disponible maintenant ici : '+ str(lien) + str(hashtag) + str(twitterUser) + "\n"
            api.update_status(aTweeter)
            time.sleep(60)
        
    elif dico[site][0] == "peertube":
        date, titre, lien = fluxRSSPeer(dico[site][3],dico[site][1])
        print(date)
        print(dico[site][1])
        hashtag = " #" + hashtagMulti(dico[site][4])
        if dico[site][2] != " ": 
            twitterUser = " @" + dico[site][2]
        elif dico[site][2] == " ":
            twitterUser = " "          
        if int(dateReel) - 3 == int(date):
            aTweeter = "Bonjour, une nouvelle video est sortie sur la chaine #Peertube: " + str(dico[site][1]) + ',  disponible maintenant ici : ' + str(lien) + str(hashtag) + str(twitterUser) + "\n"
            api.update_status(aTweeter)
            time.sleep(60)

            
