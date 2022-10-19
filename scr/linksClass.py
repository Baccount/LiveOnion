import re
import socket

import requests
import socks
from bs4 import BeautifulSoup


class Links:
    """Class that downloads the links from from the search results"""

    def __init__(self, url):
        self.url = url
        self.links = []

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

        res = requests.get(self.url)

        # Using beautifulsoup to get the website content into a nice format

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
