import tweepy

auth = tweepy.OAuthHandler("PrVAMU3WgCL8yRyU0P8fnc1yU", "NUkAq6Y16N5FrPX2hsvRAQcn3B0mU85b3xyzHUmMpu0Vt6otBo")
auth.set_access_token("947744588697042945-AVjCrdprkbLGDr8RCxMC3XmO6ehQDXr", "KtioiJD8RNTHMvBSCce4VXnD1bqKTbym9Z1fwYNmXaveR")

api = tweepy.API(auth)

public_tweets = api.home_timeline()

print(public_tweets)
for tweet in public_tweets:
    print(tweet.text)
    
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "PrVAMU3WgCL8yRyU0P8fnc1yU",
    "consumer_secret"     : "NUkAq6Y16N5FrPX2hsvRAQcn3B0mU85b3xyzHUmMpu0Vt6otBo",
    "access_token"        : "947744588697042945-AVjCrdprkbLGDr8RCxMC3XmO6ehQDXr",
    "access_token_secret" : "KtioiJD8RNTHMvBSCce4VXnD1bqKTbym9Z1fwYNmXaveR" 
    }

  api = get_api(cfg)
  tweet = "Congrats to St. Peters"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
    
 