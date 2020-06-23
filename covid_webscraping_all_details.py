import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import re
import time

# Extracting the full article content from each URL
df = pd.read_excel('covid.xlsx')
# df = df[df.Title != "COVID-19: Government identifies 170 hotspot districts"]
# df = df[df.Title != "Covid-19 pandemic: Muslims will observe Ramzan in their homes, avoid gatherings"]
# df = df[df.Title != "Covid-19 in Maharashtra: Cop posted outside CM's residence tests positive"]

df['All_content'] = ''
session_requests = requests.session()
for index, row in df.iterrows():
    url = row['Article URL']
    try:
        result = session_requests.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')
        
        results = soup.find(class_ = 'Normal')
        # if(results == None):
        #     continue
            
        results = results.text.strip('\t\r\n')
        results = re.sub(r'[\t\r\n]', ' ', results)
        
        df.at[index,'All_Content'] = results
        #row['All_Content'] = results
        #df1 = df1.append({'All_Content': results}, ignore_index=True)
        print(row['Title'])
        print(results)
        print("\n")
        time.sleep(0.4)

    except:
        continue
    

# df=df.join(df1)
df = df.drop('Unnamed: 0',axis=1)
df.to_excel('covid1.xlsx')
#df.to_csv('covid1.csv')

