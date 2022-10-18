from tools import s_input

def main():
    ''' Main function '''
    # get the users search engine choice
    choice = s_input()
    # get the users search query
    query = query_input()
    # build the search url
    url = choice + query
    



if __name__ == '__main__':
    main()