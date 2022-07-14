import requests

URL = 'http://127.0.0.1:5000'

response = requests.post(f'{URL}/post/', json={'head': 'Ford focus 3 for sale',
                                              'description': 'The car was released in 2014. Still in good conditions.',
                                              'owner': 'Yura'})

# get_one = requests.get(f'{URL}/adv/1/')

# print(get_one.json())
print(response.status_code)
print(response.json())
