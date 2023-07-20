# Create a program that allows you to search for gifs

import requests

# ask the user about the search request
search_request = input('Hey! If you want to search for GIFs \
just enter the word to search: ')
search_request = search_request.replace(' ', '+')


# ask the user about the output amount with negative values and max check
def change_to_max() -> int:
    try:
        output_limit = int(input('Okay how many images you want? (max - 30):'))
    except ValueError:
        return print('Sorry, you entered nothing.')

    if output_limit > 30:
        return 30
    elif output_limit <= 0:
        return 1
    else:
        return output_limit


# form the payload of params to add into endpoint URL with request
search_payload = {'api_key': 'HZ4EDtMVzaqRP7uhuuLDfDzl8S2wphO6',
                  'q': search_request,
                  'limit': change_to_max(),
                  'offset': 0,
                  'rating': 'g',
                  'lang': 'en'
                  }

# make a request and save the output in JSON
r = requests.get('https://api.giphy.com/v1/gifs/search', params=search_payload)
results = r.json()

# print all links
try:
    for i in range(0, search_payload['limit']):
        print(results['data'][i]['images']['original']['url'])
except IndexError:
    print('Sorry, nothing found. Try another search request pls')
except TypeError:
    print('Try to use the script again')
