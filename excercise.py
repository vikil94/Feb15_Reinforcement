def accesible_toronto(venues, accessible, city, capacity):
    new_venues = []
    for i in venues:
        if i['wheelchair_accessible'] and i['city'] == city and i['capacity'] >= capacity:
            new_venues.append(i)
    return new_venues

venues = [
{ 'address': "123 Main Street", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 100 },
{ 'address': "567 Centre Street", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 400 },
{ 'address': "9B Ontario Street", 'city': "Montreal", 'wheelchair_accessible': True, 'capacity': 1000 },
{ 'address': "56 Road Avenue", 'city': "Ottawa", 'wheelchair_accessible': True, 'capacity': 650 },
{ 'address': "938 Avenue Way East", 'city': "Toronto", 'wheelchair_accessible': False, 'capacity': 90 },
{ 'address': "34 Main Street West", 'city': "London", 'wheelchair_accessible': False, 'capacity': 300 },
{ 'address': "44 Quebec Road", 'city': "Toronto", 'wheelchair_accessible': True, 'capacity': 200 },
{ 'address': "10 Spruce Avenue Ouest", 'city': "Montreal", 'wheelchair_accessible': False, 'capacity': 525 }

]

new_venues_list = accesible_toronto(venues, True, "Toronto", 150)
print("This is the new list of venues that are in toronto are wheelchair accessible and have a capacity of 150 or more: {}".format(new_venues_list))
