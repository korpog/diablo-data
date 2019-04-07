import json
import requests
from datetime import datetime
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

def get_access_token():
    """ Get access token required to use Blizzard's API. """
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)
    
    client_id = credentials['CLIENT_ID']
    client_secret = credentials["CLIENT_SECRET"]

    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://us.battle.net/oauth/token', client_id=client_id,
        client_secret=client_secret)
    access_token = token['access_token']
    return access_token

def get_data(region, class_name, season, gamemode=''):
    """
    Get data from Blizzard's API. Returns a Python object representing JSON data.
    Allowed argument values:
    region: us, eu, kr
    class_name: barbarian, dh, monk, wizard, wd, necromancer
    season: 1 to 16 (as of February 2019)
    gamemode: 'hardcore-' or '' (default value)
    """

    token = get_access_token()
    r = requests.get(f'https://{region}.api.blizzard.com/data/d3/season/{season}/leaderboard/rift-{gamemode}{class_name}?access_token={token}')
    data = json.loads(r.text)
    return data

def process_data():
    data = get_data('us', 'dh', 1)
    with open('dh.json', 'w') as file:
        json.dump(data, file)
    records = []
    for row in data['row']:
        battletag = row['player'][0]['data'][0].get('string', 'unknown')
        rank = row['data'][0]['number']
        rift_level = row['data'][1]['number']
        time = row['data'][2]['timestamp']
        date = row['data'][3]['timestamp']
        date = datetime.fromtimestamp(date / 1e3)
        record = {'Rank': rank, 'Rift level': rift_level, 'Time': time, 'Completed on': date.strftime("%c"), 'Battletag': battletag}
        records.append(record)
    print(records[:2])

process_data()