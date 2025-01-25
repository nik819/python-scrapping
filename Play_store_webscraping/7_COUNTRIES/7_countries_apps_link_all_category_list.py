import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.common.by import By
import re   
import scrape_top_charts as charts

df = pd.read_csv('C:/Users/kc/Desktop/Play_store_webscraping/play_store_categories.csv')
data = pd.DataFrame(columns=df['category'])
column = data.columns

cnt = pd.read_csv("play_store_country.csv")
countries = {}
for i in range(len(cnt["Country_Name"])):
    countries[cnt["Country_Name"][i]] = cnt["Country_code"][i]

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def scrape_play_store_category_links(country_code):
    for i in range(0,len(df['category'])):
        charts.top_charts = {
        "link":[],
        "title":[]
        }
        top_chart_links = list()
        URL = "https://play.google.com/store/apps/category/"+df['category'][i]+"?gl="+country_code
        top_charts = charts.scrape_google_play_apps(URL)
        for j in top_charts["link"]:
            top_chart_links.append(j) 

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(URL)
        time.sleep(5)

        SCROLL_PAUSE_TIME = 2
        
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(SCROLL_PAUSE_TIME)
        
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
        
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        links_games = list()  
        
        #elems = driver.find_elements(By.XPATH,"//a[@href]")
        elems = driver.find_elements(By.CLASS_NAME,"Si6A0c")
        for elem in elems:
            if "details?id" in elem.get_attribute("href"):
                links_games.append((elem.get_attribute("href")))
                
        #links_games = list(dict.fromkeys(links_games))
        
        lnk = list()
        combine_link = top_chart_links + links_games
        for x in combine_link:
            if x not in lnk:
                lnk.append(x+'&gl='+country_code+'&hl=ar')
        print(lnk)
        data[column[i]]=pd.Series(lnk)   
def country_choice():
    print("Enter Country Name : ")
    country = input()

    c = country.title()
    cnt_code = ''
    for i in countries.keys():
        if c in i:
            cnt_code = countries[i]
    return cnt_code

country_code = country_choice()     
scrape_play_store_category_links(country_code)
# fnm = 'links_per_category.csv'
# with open(fnm,'w') as csvfile:
data.to_csv('C:/Users/kc/Desktop/Play_store_webscraping/7_COUNTRIES/'+country_code+'_apps_link_all_category.csv',index=False)