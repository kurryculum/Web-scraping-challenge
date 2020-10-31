#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
from bs4 import BeautifulSoup as bs
import requests 
import json
from splinter import Browser
import time
import urllib.request
import ssl

# from selenium import webdriver

ssl._create_default_https_context = ssl._create_unverified_context
    
    


# In[2]:


#news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

#news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."


# In[3]:


# URL of page to be scraped
    

    # In[4]:


    # Retrieve page with the requests module
def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()

    url= 'https://mars.nasa.gov/news'


    browser.visit(url)
    time.sleep(3)
    html = browser.html


    # In[5]:


    # Create BeautifulSoup object; parse with 'html.parser'
    soup = bs(html, 'html.parser')


    # In[6]:


    # Examine the results, then determine element that contains sought info
    # print(soup.prettify())


    # In[7]:


    news_title = soup.find_all("div", class_='content_title')[1]
    news_title.text


    # In[8]:


    p_tags=soup.find_all("li", class_="slide")[0]
    p_tags.text


    # In[9]:


    url= 'https://mars.nasa.gov/news'


    # In[10]:


    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'


    # In[11]:


    # # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    # get_ipython().system('which chromedriver')


    # In[12]:


    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[13]:


    browser.visit(image_url)
    html = browser.html


    # In[14]:


    i_url = soup.find_all("img")[5]["src"]


    # In[15]:


    featured_image_url=url+i_url
    # print(featured_image_url)


    # In[16]:


    url= 'https://space-facts.com/mars'


    # In[17]:


    tables = pd.read_html(url)
    tables


    # In[18]:


    type(tables)


    # In[19]:


    df=tables[0]
    df.head()


    # In[20]:


    df.columns


    # In[21]:


    df1 = df.rename(columns={0:"description",1:"values"})
    df2=df1.set_index("description")
    df2


    # In[22]:


    # dataframe to html


    # In[23]:


    html_table = df2.to_html()


    # In[24]:


    # strip and clean the table 
    html_table.replace('\n','')


    # In[25]:


    mars_df = df2.to_html(classes = 'table table-striped')
    # print(mars_df)


    # In[26]:


    # get_ipython().system('open table.html')


    # In[46]:


    mars= {"news_title":"News_Title","p_tags":"news_p","featured_img_url":"https://mars.nasa.gov/news/system/missions/list_view_images/2_PIA14175-thmfeat.jpg","html_table":"Mars_table"}
    mars


    # In[27]:


    astrology_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(astrology_url)
    hem_html = browser.html


    # In[28]:


    soup = bs(hem_html, 'html.parser')
    # print(soup.prettify())


    # In[29]:


    

    # In[30]:


    browser.find_by_css('.itemlink')


    # In[31]:


   


    # In[32]:



    # In[43]:


    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
        {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"},
    ]


    # In[45]:


    image_dict = {}
    image_dict ["title"]=title
    image_dict ["image_url"]=image_url
    hemisphere_image_urls.append(image_dict)
    # print(hemisphere_image_urls)


    # In[47]:


    mars_dict = {
            "news_title": news_title,
            "news_p": p_tags,
            "featured_image_url": featured_image_url,
            "mars_fact_table": mars_df,
            "hemisphere_images": hemisphere_image_urls
        }
    # print(mars_dict)
    
    y = mars_dict
    return y


    # In[89]:



    # In[92]:




    # In[ ]:




