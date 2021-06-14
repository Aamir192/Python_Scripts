import time
import hashlib
import requests

API_TOKEN = "3942d0c6-bee1-11eb-8ebc-06454ba65feb"
API_URL = 'https://nbttest.vmlyr.com/nbt/rs/search/opportunities?query={"count":0,"modified":{"start":{"value":"2021-05-11T00:05:02Z"}},"sortOrder":"asc","lobs":["1"]}'
FILE_LOCATION = "C:/Users/Asus/Desktop/Aamir/json.txt"


def generate_authorization_key(timestamp, token):
    input_string = str(timestamp) + token
    hash = hashlib.sha512(str(input_string).encode("utf-8")).hexdigest()
    return hash


def download_data():
    timestamp = format(time.time() * 1000, '.0f')
    authorization_key = generate_authorization_key(timestamp, API_TOKEN)
    querystring = {
        "query": "{\"count\":0,\"modified\":{\"start\":{\"value\":\"2021-05-11T00:05:02Z\"}},\"sortOrder\":\"asc\",\"lobs\":[\"1\"]}"}

    headers = {
        'authorization': authorization_key,
        'timestamp': timestamp,
        'cache-control': "no-cache",
    }

    response = requests.request("GET", API_URL, headers=headers, params=querystring)

    with open(FILE_LOCATION, 'w+') as f:
        f.write(response.text)
    
    print(dir(f))



if __name__ == '__main__':
    download_data()
