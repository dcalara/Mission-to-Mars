from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from pprint import pprint

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

# # Mars News
# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

# In[22]:


    mars_dict = {}
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    time.sleep(1)
# scrape into soup
    html = browser.html
    soup = bs(html, "html.parser")
# get title
    title = soup.find("div", class_="content_title").text
# get paragraph
    paragraph = soup.find("div", class_="article_teaser_body").text
    print(title) 
    print(paragraph)
    mars_dict['new_title'] = title
    mars_dict['news_paragraph'] = paragraph


# In[23]:


    mars_dict



# In[4]:

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    time.sleep(1)


# In[5]:



# click full image
    browser.find_by_id('full_image').click()

# click more info



# In[9]:


    more_info = browser.find_link_by_partial_text('more info')
    more_info.click()


# In[10]:


    html = browser.html
    jpl_soup = bs(html, "html.parser")


# In[11]:


    featured_img = jpl_soup.find('figure', class_='lede').a.img


# In[12]:


    featured_img['src']


# In[24]:


    featured_image_url = 'https://www.jpl.nasa.gov' + featured_img['src']
    mars_dict['featured_image_url'] = featured_image_url


# # Mars Weather

# In[25]:
#browser = Browser("chrome", **executable_path, headless=False)
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
# scrape into soup
    html = browser.html
    soup = bs(html, "html.parser")
# get tweet text
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)
    mars_dict['mars_weather'] = mars_weather


# # Mars Facts

# In[26]:


    url = "https://space-facts.com/mars/"
    browser.visit(url)
    df = pd.read_html(url)[0]
    mars_facts_html = df.to_html()
    pprint(mars_facts_html)
    mars_dict['mars_facts_html'] = mars_facts_html


# # Mars Hemispheres


# In[16]:

    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
# scrape into soup
    html = browser.html
    soup = bs(html, "html.parser")

    hemisphere_image_urls = []

# In[17]:


    urls = browser.find_by_css('div.description')
    urls


# In[19]:


    for i in range(len(urls)):
        browser.find_by_css('div.description')[i].find_by_css('h3').click()
        browser.find_link_by_text('Sample').first
        hemisphere = {}
        hemisphere['title']=browser.find_by_css('h2.title').text
        hemisphere['href']=browser.find_link_by_text('Sample').first['href']
        hemisphere_image_urls.append(hemisphere)
        print(hemisphere)
        browser.back()


# In[20]:


    hemisphere_image_urls


# In[27]:


    mars_dict['hemisphere_image_urls'] = hemisphere_image_urls





