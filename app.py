import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from validator_collection import validators, checkers
import eventlet
import sys

# default values
example_url = 'https://www.mlssoccer.com/players/mikey-ambrose'
timeout_value = 3

# main function
def main():
    try:
        url=sys.argv[1]
        get_img_url(url)
    except:
        get_img_url(example_url)

# retrieve url of player's image given the url with the player's general information from the mlssoccer website
def get_img_url(my_url):
    if(check_valid_input(my_url)):
        try:
            page_soup = make_connection(my_url, timeout_value)
            try:
                img = page_soup.findAll('img', {'class': 'headshot_image'})    
                img_url = img[0]['src']
                img_url = img_url[:img_url.find("?")]
                print(img_url)
                return img_url
            except:
                print("please enter the soccer url")
                return
        except:
            print("Failed to access url!")
            print("please enter an existing url")
            return
    else:
        print("please enter a valid url")
        return

# check if input is in the format of a url
def check_valid_input(my_url):
    return checkers.is_url(my_url)

# make connection and verify that url is an actual endpoint (times out after 5 seconds, the default value)
def make_connection(my_url, timeout_input):
    uClient = uReq(my_url, timeout=timeout_input)
    page_html = uClient.read()
    uClient.close()
    return soup(page_html, "html.parser")

main()