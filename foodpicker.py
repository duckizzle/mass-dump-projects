import random

food = [
    'McDonalds',
    'Wendys',
    'Five Guys',
    'Burger King',
    'Chipotle',
    'Just make something at home, forehead',
    'Papa Johns',
    'Noodles & Co.',
    'Aroogas'
]

# random.randint(1, 5) --> random number between 1 and 5
# random.choice(array) --> random item in this array

selected = random.choice(food)

print('What should I order today?')
print(selected)