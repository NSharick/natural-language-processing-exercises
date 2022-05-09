## Acquire Functions Web Scraping

#imports
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

#CodeUp blog posts
def parse_individual_post(article):
    '''
    This function takes in the html code produced by the get_blog_posts function and 
    returns a dictionary with the title and the content of the article
    '''
    output = {}
    output['title'] = article.select_one('h1').text
    output['content'] = article.select_one('div.entry-content').text.strip()
    return output

def get_blog_posts(url):
    '''
    This function takes in a url for an individual blog post and returns the 
    html code that can be scraped using the parse_individual_post function
    '''
    url = url
    headers = {'user-agent': 'Innis Data Science Cohort'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('article.et_pb_post')
    article = articles[0]
    dict = parse_individual_post(article)
    return dict




#InShorts news articles
def parse_news(article, category):
    '''
    This function takes in the html from an article and a category name and 
    outputs a dictionary with the article title, content and category
    '''
    output = {}
    output['title'] = article.select_one('div.news-card-title').text.strip()
    output['content'] = article.select_one('div.news-card-content').text.strip()
    output['category'] = category
    return output


def get_news_articles(url, category):
    '''
    This function takes in a url and a category name and outputs a dataframe with the title and content 
    from all the articles on that page using the parse_news function to pull the data from the html
    '''
    response = get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('div.news-card')
    df = pd.DataFrame([parse_news(article, category) for article in articles])
    return df
