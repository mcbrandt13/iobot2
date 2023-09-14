#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import requests
import random

@respond_to('hello$', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello sender!')


@respond_to('^reply_webapi$')
def hello_webapi(message):
    message.reply_webapi('hello there!', attachments=[{
        'fallback': 'test attachment',
        'fields': [
            {
                'title': 'test table field',
                'value': 'test table value',
                'short': True
            }
        ]
    }])


@respond_to('^reply_webapi_not_as_user$')
def hello_webapi_not_as_user(message):
    message.reply_webapi('hi!', as_user=False)


@respond_to('hello_formatting')
def hello_reply_formatting(message):
    # Format message with italic style
    message.reply('_hello_ sender!')


@listen_to('hello$')
def hello_send(message):
    message.send('hello channel!')


@listen_to('hello_decorators')
@respond_to('hello_decorators')
def hello_decorators(message):
    message.send('hello!')

@listen_to('hey!')
def hey(message):
    message.react('eggplant')


@respond_to(u'你好')
def hello_unicode_message(message):
    message.reply(u'你好!')


@listen_to('start a thread')
def start_thread(message):
    message.reply('I started a thread', in_thread=True)

@respond_to('say hi to me')
def direct_hello(message):
    message.direct_reply("Here you are")

@respond_to("^bs")
def generate_bs(message):
    """bs: Generate some corporate bs."""
    r = requests.get('http://kpbrandt.com/api/bs')
    message.reply(r.json().get('msg'))

@respond_to("^shut it down")
def shut_it_down(message):
    message.reply('https://imgur.com/Y4GCgDu')

@respond_to("^haha yes")
def haha_yes(message):
    message.reply('http://kpbrandt.com/static/kpbrandt/images/sickos.jpg')

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
    message.reply("%s" % img_url)