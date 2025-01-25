import pandas as pd

df = pd.DataFrame(columns=['Country','ART_AND_DESIGN','AUTO_AND_VEHICLES','BEAUTY','BOOKS_AND_REFERENCE','BUSINESS','COMICS',
'COMMUNICATION','DATING','EDUCATION','ENTERTAINMENT','EVENTS','FINANCE','FOOD_AND_DRINK','HEALTH_AND_FITNESS',
'HOUSE_AND_HOME','LIBRARIES_AND_DEMO','LIFESTYLE','MAPS_AND_NAVIGATION','MEDICAL','MUSIC_AND_AUDIO',
'NEWS_AND_MAGAZINES','PARENTING','PERSONALIZATION','PHOTOGRAPHY','PRODUCTIVITY','SHOPPING','SOCIAL','SPORTS',
'TOOLS','TRAVEL_AND_LOCAL','VIDEO_PLAYERS','WEATHER'])

cnt = pd.read_csv("play_store_country.csv")
countries = {}
for i in range(len(cnt["Country_Name"])):
    countries[cnt["Country_Name"][i]] = cnt["Country_code"][i]


def country_choice():
    print("Enter Country Name : ")
    country = input()

    c = country.title()
    cnt_code = ''
    for i in countries.keys():
        if c in i:
            cnt_code = countries[i]
    return cnt_code

def total_apps_counts(c_code):
    lst = list()
    df = pd.read_csv('D:/nikhil/Play_store_webscraping/7_COUNTRIES/'+c_code+'_apps_link_all_category.csv')
    column = df.columns
    for c in range(len(column)):
        cnt = column[c]
        lst.append(len(df['MAPS_AND_NAVIGATION']))
    print(lst)
    print(len(lst))


c_code = country_choice()
total_apps_counts(c_code)
