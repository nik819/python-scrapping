import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
from googletrans import Translator
import re
import openpyxl
# lst = ['books','business','developer-tools','education','entertainment','finance','food-and-drink',
#        'games','graphics-and-design','health-and-fitness','kids','lifestyle','medical','music','navigation',
#        'news','photo-and-video','productivity','reference','shopping','social-networking','sports','travel',
#        'utilities','weather']

for cat in lst:
    workbook = openpyxl.load_workbook('D:/nikhil/AppFigure_scraping/MENA COUNTRY/KUWAIT/KUWAIT_IOS.xlsx')
    sheet = workbook.create_sheet(cat)
    raw_data = [['app_name','app_link']]
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    data = pd.DataFrame(columns=['app_name','app_link'])
    URL = 'https://appfigures.com/top-apps/ios-app-store/kuwait/iphone/'+cat
    print(URL)
    driver.get(URL)
    for i in range(0,4000):
        driver.execute_script(f"window.scrollBy({i}, {i+200})","")
        i=i+200
            
    lst = list()
    nm = list()
    dic = {}
    translator = Translator()
    elems = driver.find_elements(By.TAG_NAME,'a')
    for elem in elems:
        #nm.append(elem.text)
        if elem.get_attribute('href') is None:
            pass
        else:
            if 'profile' in elem.get_attribute("href"):
                #translated_text = translator.translate((re.sub(r'\d', '', elem.text)).replace('.',''))
                #nm.append(translated_text.text)
                nm.append(elem.get_attribute("title"))
                lst.append(elem.get_attribute("href"))
    translation = translator.translate(nm,dest='en')
    title = []
    for trans in translation:
        title.append(trans.text)
    print(title)
    dic["title"] = title
    dic["url"] = lst
    df = pd.DataFrame.from_dict(dic) 
    print('total app :  ',len(df['title']))
    for j in range (len(df['title'])):
        raw_data.append([df['title'][j],df['url'][j]])
    for raw in raw_data:
        sheet.append(raw)
    workbook.save('D:/Nikhil/AppFigure_scraping/MENA COUNTRY/KUWAIT/KUWAIT_IOS.xlsx')
#print(df)
#df.to_csv('jordan_weather.csv')

#data['app_name'] = pd.Series(nm)
#data['app_link'] = pd.Series(lst)
#data.to_csv('1ios_jordan_country_lifestyle_category_app_link_list.csv')
