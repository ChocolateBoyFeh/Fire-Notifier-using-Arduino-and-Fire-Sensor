import tweepy
import serial
from datetime import datetime



data = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0
		
)

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)





def main():
  cfg = { 
    "consumer_key"        : "Bl2i8iWYkBUVnC8d8gxLzi7qV",
    "consumer_secret"     : "UiytGtdRrtLgqkTkDS36seXl4xgqxpKJ3FYLIA3Gak5rEXSwby",
    "access_token"        : "760820650550304768-muZDCNQCIX7DPRpVsycDz9Lvy57FqHD",
    "access_token_secret" : "I4kL7ePifap2I9YPw0tVHgpF3lhW2WuhViwELEhbEvbPt" 
    }

  api = get_api(cfg)
  tweet = "Your place is on fire...at "+str(datetime.now())
  status = api.update_status(status=tweet)
  print("Tweeted")
  

if __name__ == "__main__":
  while(True):
      if(data.readline() == b'Fire\r\n'):
          main()
