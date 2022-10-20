import re
import socket
import sqlite3

import requests
import socks
from bs4 import BeautifulSoup

AHMAI = (
    "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q="
)
DUCKDUCKGO = (
    "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/?hps=1&q="
)


class Links:
    """Class that downloads the links from from the search results"""

    def __init__(self):
        self.links = []
        self.query = ""
        self.engine = ""

    def get_links(self):
        """Downloads the links from the search results"""
        # Configuring Socks to use Tor

        socks.set_default_proxy(socks.SOCKS5, "localhost", 9150)
        socket.socket = socks.socksocket

        # It is necessary to use Tor for DNS resolution of Onion websites

        def getaddrinfo(*args):
            return [(socket.AF_INET, socket.SOCK_STREAM, 6, "", (args[0], args[1]))]

        socket.getaddrinfo = getaddrinfo

        # Using requests package to read in the Hidden Wiki Onion Website on the Darknet

        res = requests.get(self.engine + self.query)

        soup = BeautifulSoup(res.content, "html.parser")

        # Getting all links out of the soup and deleting None's
        self.links = [link.get("href") for link in soup.find_all("a")]
        # find all the links similar to the following format /search/search/redirect?search_term=tor&redirect_url=http://someonionaddress.onion
        # and extract the onion link from the redirect_url parameter
        self.links = [
            re.search(r"redirect_url=(.+)", link).group(1)
            for link in self.links
            if re.search(r"redirect_url=(.+)", link)
        ]
        # strip any link with adinfo in it
        self.links = [link for link in self.links if not re.search(r"adinfo", link)]
        # print the onion links
        return self.links

    def save_links(self):
        # save links to sqlite database using the query as the table name and the links as the columns
        try:
            conn = sqlite3.connect("links.db")
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS {0} (link text)".format(self.query))
            for link in self.links:
                c.execute("INSERT INTO {0} VALUES (?)".format(self.query), (link,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e + "Error saving links to database")

    def read_links(self):
        # read links from sqlite database using the query as the table name
        conn = sqlite3.connect("links.db")
        c = conn.cursor()
        c.execute("SELECT * FROM {0}".format(self.query))
        links = c.fetchall()
        conn.close()
        return links

    def __str__(self):
        return str(self.links)

    def set_engine(self):
        """Returns users search engine choice"""
        # dark engine search engines
        print("1. Ahmia\n2. DuckDuckGo")
        choice = input(": ")
        if choice == "1":
            self.engine = AHMAI
        elif choice == "2":
            self.engine = DUCKDUCKGO

    def set_query(self):
        """Sets users search query"""
        self.query = input("Search: ")

    def print_links(self):
        """Prints the links"""
        for link in self.links:
            print(link)
