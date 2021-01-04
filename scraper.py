"""
    A python class that will scrape a wikipedia web page.
    Has fuctions:
        - scrape_wiki_article
            -> Will get all links within a wikipedia article
        - filter_link
            -> Will filter out the link to exclude certain file types and wikipedia specific links
        - save_links
            -> Save all links into NOTES.txt
"""

import requests #for handleing requests
from bs4 import BeautifulSoup #Used to parse the web page

class Scrape():
    def __init__(self, url = ""):
        url = "https://en.wikipedia.org" + url
        self.scraped_articles = self.scrape_wiki_article(url)

    #? Scrapes wikipedia link ?#
    def scrape_wiki_article(self, url):

        """
        Input:
            -> Will accept a url in the form of https://en.wikipedia.org/wiki/...
        Process:
            -> Grabs all <a> tags within the HTML
            -> Extracts everything after the href=""
            -> Filters by Domain and File type
        Output:
            -> Will output a list of links in the form of ["/wiki/..."]
        """

        response = requests.get(url=url)
        soup = BeautifulSoup(response.content, 'html.parser')

        #? Grab all main links within that article ?#
        scraped_links = soup.find(id="bodyContent").find_all("a")

        links = []
        #? Will filter out links and then output to a file ?#
        for link in scraped_links:
            try:
                if self.filter_link(link['href']) is None:
                    continue
                links.append(self.filter_link(link['href']))
            except KeyError:
                pass
        #self.save_links(links)
        return links
    
    #? Filters out wikipedia links ?#
    def filter_link(self, link):
        """
        Input:
            -> Accepts a link in the form of a string
        Process:
            -> Will check for certain words/file extensions then check the Domain of the site
        Output:
            -> A link in the form of a string
        """
        banned_links = ["svg", "png", "jpg", "JPG", "Category:"]
        if any(extension in link for extension in banned_links): #? Checks against banned links ?#
            return None
        #! MAKE SURE TO CHECK FOR WIKIPEDIA DOMAIN FIRST !#
        if link.find("/wiki/") == -1: #? If link is not a wikipedia link, continue ?#
            return None
        if not link.startswith("/wiki/"): #? Checks to see if it iw part of the wikipedia domain ?#
            return None
        return link

    #? Saves wikipedia article links onto a file ?#
    def save_links(self, links):
        """
        Input:
            -> A list of links
        Process:
            -> Saves links to a file
        Output:
            -> A file containing links
        """
        with open("links.txt", "w") as file_of_lists:
            for link in links:
                file_of_lists.write("%s \n" % link)