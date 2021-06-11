from datetime import datetime
from six import iteritems
import tweepy
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import pyperclip
from selenium.webdriver import ActionChains
import sys
from pyshorteners import Shortener
auth = tweepy.OAuthHandler('', '') #add your API Key and Secret
auth. set_access_token('', '') #add your Access Token and Secret
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def idreplace():
    with open('/lastmen.txt', 'w') as replace: # locate lastmen.txt file in your system
        replace.write(str(idSTR))
        replace.close()

def gettinglink():
    options = webdriver.ChromeOptions()
    time.sleep(1)
    options.add_argument('Headless')
    time.sleep(1)
    driver = webdriver.Chrome(executable_path='/chromedriver', chrome_options= options) # locate chromedriver file in your system
    time.sleep(1)
    driver.get('https://7ammel.net/')
    time.sleep(1)
    link = driver.find_element_by_name("url")
    time.sleep(1)
    link.send_keys(lastmentionvideo)
    link.send_keys(Keys.ENTER)
    time.sleep(1)
    global url
    url = driver.current_url
    driver.close()


def snedlink():
    api.update_status(status = 'There you go! \ndont forget to follow me \n \n'+ shortu, in_reply_to_status_id = idSTR, auto_populate_reply_metadata = True)
    print('\ntweet has been replyed to!')
    print(lastmention, '\n')

def arch():
    with open('/all_tweets.txt', 'a') as append: # locate all_tweets.txt files in your system
        append.write(str(datetime.now()))
        append.write(" ")
        append.write(lastmention)
        append.write(" ")
        append.write('\n')
        append.close()

def urlshort():
    s = Shortener()
    global shortu
    shortu = s.tinyurl.short(url)
while True:
    try:
        lastmen = api.mentions_timeline(count = 1) # count is number of mentions the bot will retreve
        for mention in reversed(lastmen):
            lastmention = 'last tweet = ' + 'https://twitter.com/' + mention.user.screen_name + '/status/' + str(mention.id) 
            lastmentionvideo = ('https://twitter.com/' + mention.in_reply_to_screen_name + '/status/' + str(mention.in_reply_to_status_id))
            with open ('/lastmen.txt', 'r') as idcheck: # locate lastmen.txt file in your system
                idSTR = str(mention.id)
                idcheckSTR = str(idcheck.read())
                if idSTR > idcheckSTR:
                    gettinglink()
                    urlshort()
                    snedlink()
                    idreplace()
                    arch()
                else:
                    print('old tweet, wating for new mentions...')
                    time.sleep(60)
                idcheck.close()
    except tweepy.TweepError as e:
        print(e.reason, '\n')
        time.sleep(5)