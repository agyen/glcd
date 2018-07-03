import tweepy
import pyowm
import time
import datetime

def tweet_Update():
    consumer_key = "PrVAMU3WgCL8yRyU0P8fnc1yU",
    consumer_secret ="NUkAq6Y16N5FrPX2hsvRAQcn3B0mU85b3xyzHUmMpu0Vt6otBo",
    access_token  =     "947744588697042945-AVjCrdprkbLGDr8RCxMC3XmO6ehQDXr",
    access_token_secret = "KtioiJD8RNTHMvBSCce4VXnD1bqKTbym9Z1fwYNmXaveR"
    
     # OAuth twitter process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
     
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    
    owm = pyowm.OWM('3817f5e71da546936ec5da9c401e9f44')
    obs = owm.weather_at_place('Cape Coast,GH')
    w = obs.get_weather()
    temp = w.get_temperature('celsius')
    
    
    # time taken
    localtime = datetime.datetime.now()
    message = "Weather Update from Cape Coast "+str(localtime) +" :\n"+"The Temp is: " + str(temp['temp']) + " and The Humidity is: " + str(w.get_humidity())
    
    #weather message to update twitter
    api.update_status(message)

# updates twitter every hour 
while True:
    tweet_Update()
    time.sleep(3600)