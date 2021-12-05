import tweepy
import requests
import sys

hash_tag = "#cutedogs #DogsofTwittter #Puppies"

token = sys.argv[1]
token_secret = sys.argv[2]
consumer_key = sys.argv[3]
consumer_secret = sys.argv[4]



# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(token, token_secret)


# Create API object
api = tweepy.API(auth)


url = "https://random.dog/woof.json?filter=mp4,webm"

def download_image():
    data = requests.get(url).json()
    content = requests.get(data['url']).content
    img_path = f"image.{data['url'].split('.')[-1]}"
    with open(img_path, 'wb') as file:
        file.write(content)
        file.close()
    
    return img_path


file_path = download_image()
media = api.media_upload(file_path)
api.update_status(status=f"How is this dog ??\n{hash_tag}", media_ids=[media.media_id])




