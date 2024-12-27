import uuid
import json
import time
import logging
from confluent_kafka import Producer

def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():

    producer = Producer({'bootstrap.servers': 'localhost:9092'})

    while True:
        try:
            res = get_data()
            res = format_data(res)

            producer.produce('users_created', json.dumps(res))
            producer.flush()
            print("Message published -> ", json.dumps(res))
            time.sleep(2)  # delay between messages
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue


if __name__ == "__main__":
    stream_data()