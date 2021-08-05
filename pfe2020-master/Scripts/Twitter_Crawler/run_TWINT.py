from Twint_pkge import clean_data, get_profile_infos, get_timeline_by_username
from tqdm import trange
key_words = ["#lovemylife", "#lifeisgood", "#happyme"]
data = clean_data(key_words)
for i in trange(len(data)):
    get_profile_infos(data['username'].iloc[i])
    print('Okay profile'+str(i))
    get_timeline_by_username(data['username'].iloc[i])
