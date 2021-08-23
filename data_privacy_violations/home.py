# -*- coding: utf-8 -*-

import PySimpleGUI as sg      
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from PIL import Image, ImageTk
import io
import send_tweet
import check_privacy
access_token = "2158465844-TYtigqXGBQa5KzshKjz5MFO9SqTVkc03FQLL37N"
access_token_secret = "ClgQD5kCml8yb70ZlseUQIXOAM6bltOwoPuD5Z3SWguXW"
consumer_key = "IaIdBOJa7ZwNI6xHS11Jg5DVb"
consumer_secret = "IuZ4G5wrK2aYU1yuOwbPqu6G0Rx1hBgHwo6xEOHANhA4gTzJv9"
# Very basic window.  Return values as a list      
def base64_to_style_image(base64_image):
    return "url('data:image/png;base64,"+base64_image+"')"
def get_img_data(f, maxsize=(100, 75), first=False):
    """Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
screen_name = api.auth.get_username()
image_elem = sg.Image(data=get_img_data('twitter-logo.jpg', first=True))

layout = [  [image_elem],
            [sg.Text("User Logined As : "+screen_name)],      
            [sg.Text('Tweet', size=(15, 1)), sg.Multiline('')],      
            [sg.Submit(), sg.Cancel()]      
            ]    
  
window = sg.Window('Twitter Home page').Layout(layout)     
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):    
        break
    if event in (None, 'Submit'):   
        print(values)        
        msg = values[1]
        print('You entered ', msg)
        is_privacy = check_privacy.check(msg)
        if is_privacy:
            sg.Popup('This have some personal information')
        else:
            send_tweet.post(msg,api)
            sg.Popup('Tweet was posted !')
window.close()
 
