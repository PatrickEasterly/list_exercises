favorite_bars = [
    'Lloyds',
    'Manuels',
    'The Imperial'
]

best_item_at_bars = [
    'Cheap vodka',
    'Dogzilla',
    'Best staff ever'
]

bars = {
    'Lloyds': 'Cheap burbon',
    'Smiths': 'Music'
}
# use [] to look up info by keyname
# print(bars['Lloyds'])

# The .get() will not raise an exception if it can't find a key

# print(bars.get('Lloyds')) #cheap burbon

# you can pass .get() second arguments
# the second argument is returned if it can't find the key

# print(bars.get('Lloyds yeet', 'stuff')) #stuff

##### Writing useful dicionaries
# How do i store multiple values for a single key?
bars = {
    'Lloyds': {
        'item': 'cheap bourbon',
        'day': 'Tuesday'
    },
    'Manuels': {
        'item': 'Dogzilla',
        'day': 'Wednesday'
    },
    'Imperial': {
        'item': 'Philly',
        'day': ['Tuesday', 'Friday']
    }
}

places = {
    'Earth': {
        'US':{
            'Georgia': {
                'Atlanta': {
                    'work': 'DigitalCrafts'
                },
                'Savannah': {
                    'music': 'River Street'
                }
            },
            'Tennessee': {
                'Nashville': {
                    'Lunch': 'Hattie B'
                }
            }
        },
        'Europe': {
            'Germany': {
                'Berlin': {
                    'lunch': 'German name'
                },
                'Munich': {
                    'snack': 'DAS SNACK SHOP'
                }
            }
        }
    },
    'Mars': 'Red place'
}
# print(places.get('Mars'))
ga_cities = places['Earth']['US']['Georgia']

# for city in ga_cities:
#     print(ga_cities[city])   # prints the keys and the values
# for city in ga_cities:
#     print(city)              # prints the keys



# print(bars)
# How do I store more complicated data for a single key?

##### Access information
# How do I access nested information?
# how to access item in a dictionary in a list
movies = [
    {
        'title': 'Avengers: endgame',
        'release date': '2019'
    },
    {
        'title': 'Avengers: infinity dollars',
        'release date': '2020'
    }
]

# print(movies[1]['release date'])


# How do I loop through lists of dictionaries?
charges = [
    {
        'vendor': 'Kula',
        'amount': 6.36
    },
    {
        'vendor': 'Kula',
        'amount': 9.11
    },
    {
        'vendor': 'Shell',
        'amount': 4.40
    },
    {
        'vendor': 'Phone',
        'amount': 41.20
    },
    {
        'vendor': 'Yeet Inc',
        'amount': 12.02
    },
    {
        'vendor': 'Kula',
        'amount': 6.36
    }
] 
# total = 0
# for item in charges:
#     # print(item['amount'])
#     total += item['amount']
# total = round(total, 2)
# print(f'Total: ${total}')
# #version 2
# high_vendor = ''
# highest = charges[0]['amount']
# for charge in charges:
#     if charge['amount'] > highest:
#         highest = charge['amount']
#         high_vendor = charge['vendor']
# print(f'Highest charge: ${highest}')
# print(f'Highest paid vendor: {high_vendor}')


##### How do I modify a dictionary? 

# how to I store new values to a dictionary?
favorites = {}
favorites['cat'] = 'Melvin'
print(favorites['cat'])        #Melvin

# how do I update a value in an existing dictionary?
favorites['cat'] = 'Pablo'
favorites.update(cat='Sage')

print(favorites['cat'])        #sage

# how do I remove values from a dictionary? 
del favorites['cat']
# or 
favorites['cat'] = ''
print(favorites)