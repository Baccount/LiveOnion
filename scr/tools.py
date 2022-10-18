AHMAI = 'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q='
DUCKDUCKGO = 'https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/?hps=1&q='


def s_input():
    ''' Returns users search engine choice '''
    # dark engine search engines
    print('1. Ahmia\n2. DuckDuckGo')
    choice = input(': ')
    if choice == '1':
        return AHMAI
    elif choice == '2':
        return DUCKDUCKGO

def query_input():
    ''' Returns users search query '''
    return input('Search: ')