from linksClass import Links


def main():
    """Main function"""
    # get the users search engine choice
    choice = s_input()
    # get the users search query
    query = query_input()
    # build the search url
    url = choice + query
    # link class contains the links from the search results
    link = Links(url)
    links = link.get_links()
    for link in links:
        print(link + "\n")


if __name__ == "__main__":
    main()
