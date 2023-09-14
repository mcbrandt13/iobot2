import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import requests
import random

STATIC_IMG_URL = "http://kpbrandt.com/static/kpbrandt/images"

@respond_to("^U WOT M8")
def u_wot_m8(message):
    message.send(f'{STATIC_IMG_URL}/uwotm8.png')

@respond_to("^win")
def win(message):
    message.send(f"{STATIC_IMG_URL}/win.jpg")

@respond_to("^ooh")
def ooh(message):
    message.send(f'{STATIC_IMG_URL}/ooh.jpg')

@respond_to("^hmm")
def hmm(message):
    message.send(f'{STATIC_IMG_URL}/hmm.png')

@listen_to('^button')
def button(message):
    message.send('http://rs247.pbsrc.com/albums/gg140/theflooper/misc/Historyeraserbutton.jpg~c200')

@listen_to('^no sir')
def nosir(message):
    message.send('http://s2.quickmeme.com/img/66/668f2c316d8211506929d9c3d3a2a2f3d65f130d512411d186520e34d559dce7.jpg')


@respond_to("^bs")
def generate_bs(message):
    """bs: Generate some corporate bs."""
    r = requests.get('http://kpbrandt.com/api/bs')
    message.send(r.json().get('msg'))

@respond_to("^shut it down")
def shut_it_down(message):
    message.send('https://imgur.com/Y4GCgDu')

@respond_to("^haha yes")
def haha_yes(message):
    message.send(f'{STATIC_IMG_URL}/sickos.jpg')

@respond_to("image me (?P<search_query>.*)$")
def image_me(message, search_query):
    """image me ___ : Search google images for ___, and post a random one."""
    try:
        print('fetching image')
        url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyCihhigU4JWGUKlXg4P1sciZYt2G1o0qJc&cx=014491182948206670424:2ogoc1sxxsa&q={0}&searchType=image&safe=high'.format(search_query)
        r = requests.get(url)
    except Exception:
        count = 0
        pass
    count = r.json().get('queries').get('request')[0].get('count')
    if count > 3:
        n = random.choice([0,1,2])
        x = r.json()['items'][n]
    elif count < 0:
        x = {'link':'None found'}
    else:
        x = {'link': 'Barf!'}
    img_url = x['link']
    message.send("%s" % img_url)