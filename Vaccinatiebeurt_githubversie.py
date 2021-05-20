#Laatste update: 20/05/2021

from selenium import webdriver
import requests
import time
import datetime
import pync

#Geboortejaar
geboortejaar = 1965
loop = 1000000
interval = 60

def start():
    url = "https://coronatest.nl/ik-wil-me-laten-vaccineren/een-online-afspraak-maken"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    global geboortejaar

    # Hoofdmenu
    time.sleep(0.5)
    searchButton = driver.find_element_by_xpath('/html/body/app-root/div/div/app-information/div/div/div/div/div/div[4]/button[2]')
    searchButton.click()

    # Brief van huisarts?
    time.sleep(0.5)
    menuEen = driver.find_element_by_xpath('/html/body/app-root/div/div/app-form-steps/div/div[1]/div/div/app-invitation-medical-indication/form/ul/li[2]/label')
    menuEen.click()

    menuEenConfirm = driver.find_element_by_xpath('/html/body/app-root/div/div/app-form-steps/div/div[1]/div/div/app-invitation-medical-indication/form/div/div/button[2]')
    menuEenConfirm.click()

    # Corona gehad?
    time.sleep(0.5)
    menuTwee = driver.find_element_by_xpath('/html/body/app-root/div/div/app-form-steps/div/div[1]/div/div/app-have-you-tested-positive-in-the-past-six-months/form/ul/li[2]/label')
    menuTwee.click()

    menuTweeConfirm = driver.find_element_by_xpath('/html/body/app-root/div/div/app-form-steps/div/div[1]/div/div/app-have-you-tested-positive-in-the-past-six-months/form/div/div/button[2]')
    menuTweeConfirm.click()

    # Geboortejaar


    time.sleep(0.5)
    menuDrie = driver.find_element_by_xpath('//*[@id="year-of-birth"]')
    menuDrie.send_keys(geboortejaar)

    menuDrieConfirm = driver.find_element_by_xpath('/html/body/app-root/div/div/app-form-steps/div/div[1]/div/div/app-what-is-your-year-of-birth/form/div[2]/div/button[2]')
    menuDrieConfirm.click()

    # Bevestiging
    time.sleep(0.5)


    try:
        confirmAll = driver.find_element_by_xpath('/html/body/app-root/div/div/app-appointment-not-possible/div/div/div/div/h1')

        if confirmAll.text == "U kunt online geen afspraak maken":
            print(str(geboortejaar - 1) + "\t" + str(datetime.datetime.now()))
    except:
        print(geboortejaar)
        pync.notify(geboortejaar)
        # vul hier code in die pushnotificaties mogelijkt maakt.
        # oorspronkelijke code weggehaald vanwege zichtbaar wachtwoord.
        geboortejaar += 1

    # Browswer afsluiten
    time.sleep(0.5)
    driver.close()

i = 0

while i < loop:
    try:
        start()
        time.sleep(interval)
    except:
        print("ERROR")
        time.sleep(10)
    i += 1
