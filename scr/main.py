from tools import s_input, query_input
from linksClass import Links

def main():
    ''' Main function '''
    # get the users search engine choice
    choice = s_input()
    # get the users search query
    query = query_input()
    # build the search url
    url = choice + query
    # link class contains the links from the search results
    link = Links(url)
    print(link.get_links())



if __name__ == '__main__':
    main()