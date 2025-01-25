import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
from googletrans import Translator
import re
from itunes_app_scraper.scraper import AppStoreScraper

data = pd.DataFrame()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
scraper = AppStoreScraper()
translator = Translator()
categories = ['books','business','developer-tools','education','entertainment','finance','food-and-drink','games','graphics-and-design',
'health-and-fitness','kids','lifestyle','medical','music','navigation','news','photo-and-video','productivity','reference','shopping',
'social-networking','sports','travel','utilities','weather']

def appfigure_ios_description():
    for cat in categories:
        desc = pd.DataFrame(columns=['isGameCenterEnabled','supportedDevices','features','advisories','screenshotUrls','ipadScreenshotUrls'
        ,'appletvScreenshotUrls','artworkUrl60','artworkUrl512','artworkUrl100','artistViewUrl','kind','artistId'
        ,'artistName','genres','price','isVppDeviceBasedLicensingEnabled','sellerName','description'
        ,'primaryGenreName','primaryGenreId','genreIds','trackId','trackName','releaseDate','currency','bundleId'
        ,'currentVersionReleaseDate','averageUserRatingForCurrentVersion','userRatingCountForCurrentVersion'
        ,'averageUserRating','trackViewUrl','trackContentRating','minimumOsVersion','trackCensoredName'
        ,'languageCodesISO2A','fileSizeBytes','sellerUrl','formattedPrice','contentAdvisoryRating','releaseNotes'
        ,'version','wrapperType','userRatingCount'])

        desc1 = pd.DataFrame(columns=['isGameCenterEnabled','supportedDevices','features','advisories','screenshotUrls','ipadScreenshotUrls'
        ,'appletvScreenshotUrls','artworkUrl60','artworkUrl512','artworkUrl100','artistViewUrl','kind','artistId'
        ,'artistName','genres','price','isVppDeviceBasedLicensingEnabled','sellerName','description'
        ,'primaryGenreName','primaryGenreId','genreIds','trackId','trackName','releaseDate','currency','bundleId'
        ,'currentVersionReleaseDate','averageUserRatingForCurrentVersion','userRatingCountForCurrentVersion'
        ,'averageUserRating','trackViewUrl','trackContentRating','minimumOsVersion','trackCensoredName'
        ,'languageCodesISO2A','fileSizeBytes','sellerUrl','formattedPrice','contentAdvisoryRating','releaseNotes'
        ,'version','wrapperType','userRatingCount'])

        print('category name :   ',cat)
        data = pd.read_excel('D:/nikhil/AppFigure_scraping/OMAN/OMAN_IOS.xlsx',sheet_name=cat)
        for URL in data['app_link']:
            try:
                driver.get(URL)
                time.sleep(5)
                app_id = driver.find_element(By.CLASS_NAME,'s1901059984-0')
                a_id = app_id.text
                print(a_id)
                result = scraper.get_app_details(a_id,country='om',lang='en')
                dict_rev = dict(result)
                for dt in dict_rev:
                    desc1[dt]=(pd.Series(translator.translate(dict_rev[dt]).text))
                desc = pd.concat([desc,desc1])
            except:
                print('except part----------')
        
        print(desc)
        desc.to_csv('D:/Nikhil/AppFigure_scraping/OMAN/DESCRIPTION/'+cat+'.csv')
appfigure_ios_description()
