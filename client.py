import requests

URL = 'http://127.0.0.1:5000'

response = requests.post(f'{URL}/adv/', json={'head': 'Ford focus 3 for sale',
                                              'description': 'Машина 2014 года, в хорошем состоянии, пробег 100 тыс.км',
                                              'owner': 'Yura'})

print(response.status_code)
print(response.json())
