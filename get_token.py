from urllib import request, parse
import requests
from oauthlib.oauth2 import BackendApplicationClient
import requests_oauthlib
import json

url = 'https://id.twitch.tv/oauth2/token'
client_credentials = json.loads(open('twitch_secret.json').read())
#
#
# client = BackendApplicationClient(client_credentials['secret']['id'])
# oauth_object = requests_oauthlib.OAuth2Session(client=client)
# token = oauth_object.fetch_token(token_url=url,
#                                  client_id=client_credentials['secret']['id'],
#                                  client_secret=client_credentials['secret']['secret'])
# access_token = token['access_token']

# my_request = requests.get(url, params={
#         'client_id': client_credentials['secret']['id'],
#         'redirect_uri': 'http://localhost',
#         'client_secret': client_credentials['secret']['secret'],
#         'grant_type': 'client_credentials'
#         # 'response_type': 'code'
#     })

my_response = requests.post(url, data={
        'client_id': client_credentials['secret']['id'],
        'redirect_uri': 'http://localhost',
        'client_secret': client_credentials['secret']['secret'],
        'grant_type': 'client_credentials'
    }
)

print(my_response.text)

credentials_response = json.loads(my_response.text)

with open('acquired_token.txt', 'w') as in_file:
    in_file.write(credentials_response['access_token'])