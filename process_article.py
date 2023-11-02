import os.path
import base64
from bs4 import BeautifulSoup
import requests
import datetime
import pyttsx3
engine = pyttsx3.init()


def getText():
    if os.path.isfile("/home/chris/projects/chrisfrew.in/public/before-the-bell/report.mp3"):
        return

    oDate = datetime.date.today()
    sYear = str(oDate.year)
    sMonth = str(oDate.strftime('%m'))
    sDay = str(oDate.strftime('%d'))
    sLink = "https://edition.cnn.com/" + sYear + "/" + sMonth + "/" + sDay + "/investing/premarket-stocks-trading/index.html" # sLink variable so it can be accessed in ipython
    try:    
        oResponse = requests.get(sLink)
    except:
        print "Site not found or other error. Try again later."
        return
    
    oSoup = BeautifulSoup(oResponse.content)

    iIndex = 0
    sText = ""
    for iIndex in range(0, len(oSoup.find_all("div", {"class": "zn-body__paragraph"}))):
        sText = sText + oSoup.find_all("div", {"class": "zn-body__paragraph"})[iIndex].get_text()
        
    # for iIndex in range(0, len(oSoup.find_all("p"))):
    #     sText = sText + oSoup.find_all("p")[iIndex].get_text()

    if sText == "":
        return
    else:
        sText = sText.encode('utf-8')
        engine.say(sText)
        engine.runAndWait()
        
# main program
getText()