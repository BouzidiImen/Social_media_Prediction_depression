from UnsplashAPI import get_unsplash_images
import json

with open('Token.json') as t:
    api_key = json.load(t)
    token = api_key[ 'unsplash' ]
DepressionKeywords = [ 'Suicide', 'Sad', 'Depression', 'Stress', 'Anxiety', 'Grief', 'Despair', 'Crying' ]
for key_word in DepressionKeywords:
    get_unsplash_images(token, key_word)
DepressionKeywords = [ 'Suicide', 'Sad', 'Depression', 'Stress', 'Anxiety', 'Grief', 'Despair', 'Crying' ]
for key_word in DepressionKeywords:
    get_unsplash_images(token, key_word)
