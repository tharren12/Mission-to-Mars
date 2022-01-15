#!/usr/bin/env python
# coding: utf-8

# In[69]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[70]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[71]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[72]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[73]:


slide_elem.find('div', class_='content_title')


# In[74]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[75]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[76]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[77]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[78]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[79]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[80]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[81]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[82]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[83]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[218]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[219]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

html = browser.html
mars_soup = soup(html, 'html.parser')
title = []
img_url = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

descriptions = mars_soup.find_all('div', class_='description')


for description in descriptions:
    hemispheres = {}
    init_url = description.find('a')['href']
    jpeg_url = "https://marshemispheres.com/" + init_url
    browser.visit(jpeg_url)
    html = browser.html
    img_soup = soup(html, 'html.parser')
    source_file = img_soup.find('div', class_='downloads')
    next_file = source_file.find_all('li')[0]
    pre_file = next_file.find('a')['href']
    img_url = "https://marshemispheres.com/" + pre_file
    title = img_soup.find('h2', class_='title').text
    hemispheres = {'img_url': img_url, 'title': title}
    hemisphere_image_urls.append(hemispheres)

    browser.back()
    


# In[220]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:


# 5. Quit the browser
browser.quit()



#








