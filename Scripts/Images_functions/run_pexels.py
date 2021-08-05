from pexels import get_pexels_images

DepressionKeywords = ['Suicide', 'Sad', 'Depression', 'Stress', 'Anxiety', 'Grief', 'Despair', 'Crying']
HappyKeywords = ['Happy', 'excited']
for key_word in HappyKeywords:
    get_pexels_images(key_word)
#for key_word in DepressionKeywords:
    #get_pexels_images(key_word)
