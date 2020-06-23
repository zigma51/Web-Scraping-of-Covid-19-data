#Importing the libraries
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

# Create an empty pandas dataframe
df = pd.DataFrame(columns = ['Date-Time', 'Title', 'Content', 'Article URL'])

# Using the URL of economic times for google related news
URL = 'https://economictimes.indiatimes.com/topic/covid'

# Autoscrolling using selenium to load all the content
browser = webdriver.Chrome()
browser.get(URL)
time.sleep(1)

elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    no_of_pagedowns-=1

#time.sleep(3)
# Copying page content in html variable
html = browser.page_source

# Creating a soup object of the page content of the above mentioned webpage
soup = BeautifulSoup(html, 'html.parser')

# Finding the id of the css attribute which has all the content
results = soup.find(id='all')

# Printing a prettified ver of the data
#print(results.prettify())

# Executing till this point gave me an SSLError which was resolved by 
# adding the Anaconda/Library/Bin to system path variable

# Finding all the news articles on google
# It is divided into two classes
articles = results.find_all('div', {"class": ["clr flt topicstry", "flr topicstry"]})

#Displaying the html content of all google news articles
# for article in articles:
#     print(article, end='\n'*2)

# Displaying html content of time the news was displayed,
# the title of the article and the article content
# for article in articles:
#     # Each article is a new BeautifulSoup object.
#     # We can use the same methods on it as we did before.
#     time_elem = article.find('time')
#     title_elem = article.find('h3')
#     content_elem = article.find('p')
#     print(time_elem)
#     print(title_elem)
#     print(content_elem)
#     print()

# Displaying the textual content of the time, title and content attributes
for article in articles:
    # Each article is a new BeautifulSoup object.
    # We can use the same methods on it as we did before.
    time_elem = article.find('time')
    title_elem = article.find('h3')
    content_elem = article.find('p')
    #link for whole article
    link = article.find('a')
    link_elem = link['href']
    # Tackling the None type content problem in any 
    # aforementioned html tags
    if None in (title_elem, time_elem, content_elem):
        continue

    # Using text function to convert the html code into textual format
    # Using strip() function to remove irrelevant whitespaces
    # print(time_elem.text.strip())
    # print(title_elem.text.strip())
    # print(content_elem.text.strip())
    # print('https://economictimes.indiatimes.com/' + link_elem)
    # print()
    
    time = time_elem.text.strip()
    title = title_elem.text.strip()
    content = content_elem.text.strip()
    url = 'https://economictimes.indiatimes.com/' + link_elem

    # Entering data into the dataframe
    df = df.append({'Date-Time': time, 'Title': title, 'Content': content, 'Article URL': url}, ignore_index=True)

#print(df)

# Exporting the obtained data into excel
df.to_excel('covid.xlsx')


