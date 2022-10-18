# class that downloads the links from from the search results
class Links:
    ''' Class that downloads the links from from the search results '''
    def __init__(self, url):
        self.url = url
        self.links = []

    def get_links(self):
        ''' Downloads the links from the search results '''

        return self.links